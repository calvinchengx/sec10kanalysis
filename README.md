# sec10kanalysis

LlamaIndex GPT: deriving SEC 10K insights with external data

This is an experiment to understand the use of LLM using `llama-index` library.

## Install dependencies

```bash
pip install -r requirements.txt
```

## Get Data

```bash
./getdata.sh
```

## Run

1. Set environment variable with your `OPENAI_API_KEY` in `.env`
2. `source .env`
3. `ipython`
4. Execute in ipython `%run 10k_analysis.py`