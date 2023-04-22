# set text wrapping
from IPython.display import HTML, display
from IPython import get_ipython

def set_css():
  display(HTML('''
  <style>
    pre {
        white-space: pre-wrap;
    }
  </style>
  '''))
get_ipython().events.register('pre_run_cell', set_css)

import os
openai_api_key = os.environ.get('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = openai_api_key

from llama_index import download_loader, GPTSimpleVectorIndex
from pathlib import Path

"""### Ingest Unstructured Data Through the Unstructured.io Reader

Leverage the capabilities of Unstructured.io HTML parsing.
Downloaded through LlamaHub.
"""

UnstructuredReader = download_loader("UnstructuredReader", refresh_cache=True)

loader = UnstructuredReader()
doc_set = {}
all_docs = []
years = [2022, 2021, 2020, 2019]
for year in years:
    year_docs = loader.load_data(file=Path(f'./data/UBER/UBER_{year}.html'), split_documents=False)
    # insert year metadata into each year
    for d in year_docs:
        d.extra_info = {"year": year}
    doc_set[year] = year_docs
    all_docs.extend(year_docs)

"""### Setup Service Context"""

from llama_index import ServiceContext

service_context = ServiceContext.from_defaults(chunk_size_limit=512)

"""### Setup a Vector Index for each SEC filing

We setup a separate vector index for each SEC filing from 2019-2022.

We also optionally initialize a "global" index by dumping all files into the vector store.
"""

# initialize simple vector indices + global vector index
# NOTE: don't run this cell if the indices are already loaded! 
index_set = {}
for year in years:
    cur_index = GPTSimpleVectorIndex.from_documents(doc_set[year], service_context=service_context)
    index_set[year] = cur_index
    cur_index.save_to_disk(f'index_{year}.json')

# Load indices from disk
index_set = {}
for year in years:
    cur_index = GPTSimpleVectorIndex.load_from_disk(f'index_{year}.json', service_context=service_context)
    index_set[year] = cur_index

# NOTE: this global index is a single vector store containing all documents
# Only relevant for the section below: "Can a single vector index answer questions across years?"
global_index = GPTSimpleVectorIndex.from_documents(all_docs, service_context=service_context)
global_index.save_to_disk(f'index_global.json')

global_index = GPTSimpleVectorIndex.load_from_disk(f'index_global.json', service_context=service_context)

"""### Ask Initial Questions over a Given Year (2020)

Let's first ask some questions over the UBER 10-k for 2020! 
"""

response = index_set[2020].query("What were some of the biggest risk factors in 2020?", similarity_top_k=3)

print(response)

response = index_set[2020].query("What were some of the signifcant acquisitions?", similarity_top_k=3)

print(response)

"""### Can a single vector index answer questions across years?

If we dump all documents to a single vector store, let's test its ability to answer questions across years!
"""

# # Option 2
# risk_query_str = (
#     "Describe the current risk factors. If the year is provided in the information, "
#     "provide that as well. If the context contains risk factors for multiple years, "
#     "explicitly provide the following:\n"
#     "- A description of the risk factors for each year\n"
#     "- A summary of how these risk factors are changing across years"
# )

# Option 1
risk_query_str = "What are some of the biggest risk factors in each year?"

response = global_index.query(risk_query_str, similarity_top_k=3)

print(str(response))

"""### Composing a Graph to synthesize answers across 10-K filings (2019-2022)

We want our queries to aggregate/synthesize information across *all* 10-K filings. To do this, we define a List index
on top of the 4 vector indices.
"""

from llama_index import GPTListIndex, LLMPredictor
from langchain import OpenAI
from llama_index.composability import ComposableGraph

# set summary text for each doc
summaries = {}
for year in years:
    summaries[year] = f"UBER 10-k Filing for {year} fiscal year"

# set number of output tokens
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, max_tokens=512))
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

graph = ComposableGraph.from_indices(
    GPTListIndex,
    [index_set[y] for y in years],
    [summaries[y] for y in years],
    service_context=service_context
)

graph.save_to_disk('10k_graph.json')

graph = ComposableGraph.load_from_disk('10k_graph.json', service_context=service_context)

"""### Setting Up the Query

We query about the risk factors. We want to synthesize information across each year.
"""

risk_query_str = (
    "Describe the current risk factors. If the year is provided in the information, "
    "provide that as well. If the context contains risk factors for multiple years, "
    "explicitly provide the following:\n"
    "- A description of the risk factors for each year\n"
    "- A summary of how these risk factors are changing across years"
)

query_configs = [
    {
        "index_struct_type": "dict",
        "query_mode": "default",
        "query_kwargs": {
            "similarity_top_k": 1,
            # "include_summary": True
        }
    },
    {
        "index_struct_type": "list",
        "query_mode": "default",
        "query_kwargs": {
            "response_mode": "tree_summarize",
        }
    },
]

response_summary = graph.query(risk_query_str, query_configs=query_configs)

print(response_summary)

print(response_summary.get_formatted_sources())

# query a specific year
response_tmp = index_set[2022].query(risk_query_str)

str(response_tmp)

# query a global index
response = global_index.query(risk_query_str, similarity_top_k=4)

str(response)

