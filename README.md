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

## Example Results

```bash
In [1]: %run 10k_analysis.py
[nltk_data] Downloading package punkt to /Users/calvin/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     /Users/calvin/nltk_data...
[nltk_data]   Package averaged_perceptron_tagger is already up-to-
[nltk_data]       date!
INFO:unstructured:Reading document from string ...
INFO:unstructured:Reading document ...
INFO:unstructured:Reading document from string ...
INFO:unstructured:Reading document ...
INFO:unstructured:Reading document from string ...
INFO:unstructured:Reading document ...
INFO:unstructured:Reading document from string ...
INFO:unstructured:Reading document ...
INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total LLM token usage: 0 tokens
INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total embedding token usage: 232797 tokens
INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total LLM token usage: 0 tokens
INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total embedding token usage: 241424 tokens
INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total LLM token usage: 0 tokens
INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total embedding token usage: 257154 tokens
INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total LLM token usage: 0 tokens
INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total embedding token usage: 246480 tokens
INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total LLM token usage: 0 tokens
INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total embedding token usage: 977855 tokens
INFO:llama_index.token_counter.token_counter:> [query] Total LLM token usage: 2102 tokens
INFO:llama_index.token_counter.token_counter:> [query] Total embedding token usage: 11 tokens


Some of the biggest risk factors in 2020 included: privacy and cybersecurity risks associated with increased remote working; legal and regulatory challenges related to the COVID-19 pandemic, including potential fines or other enforcement measures resulting from the launch of new services, features, or health and safety requirements; financial impacts from the COVID-19 pandemic, including workforce reductions and changes to pricing models; the uncertainty of the pandemic's cumulative and ultimate impact on our future business operations, liquidity, financial condition, and results of operations; the duration of the spread of the outbreak and any future “waves” or resurgences of the outbreak or variants of the virus, both globally and within the United States, the impact on capital and financial markets, foreign currencies exchange, governmental or regulatory orders that impact our business and whether the impacts may result in permanent changes to our end-users’ behaviors; the potential for weak demand for our Mobility offering for a significant length of time; the timing of widespread adoption of vaccines against COVID-19 in the United States or internationally; the impact the COVID-19 pandemic will have on our business partners and third-party vendors; the extreme volatility in financial markets; and the potential for cascading effects of the pandemic that are
INFO:llama_index.token_counter.token_counter:> [query] Total LLM token usage: 2285 tokens
INFO:llama_index.token_counter.token_counter:> [query] Total embedding token usage: 11 tokens


Some of the significant acquisitions mentioned in the context information include the divestiture of our ATG business to Aurora, the divestiture of our Uber Elevate business to Joby, the Yandex.Taxi joint venture in Russia/CIS, the agreement to enter into a joint venture with SK Telecom Co., LTD., the acquisition of Careem, the purchase of a controlling interest in Cornershop, the acquisition of Routematch Holdings, Inc., the acquisition of Postmates Inc., the divestiture of Uber Eats India to Zomato, and the divestiture of certain assets of our JUMP business and investment in Lime. These acquisitions resulted in the recognition of $2.5 billion in goodwill in our Mobility segment, $540 million in intangible assets, $384 million in goodwill in our Delivery segment, $122 million in intangible assets, $91 million in goodwill in our Mobility segment, $27 million in intangible assets, and $3.1 billion in goodwill in our Delivery segment and $1.0 billion in intangible assets. Refer to Note 18 – Business Combinations for further information of our acquisitions.
INFO:llama_index.token_counter.token_counter:> [query] Total LLM token usage: 3026 tokens
INFO:llama_index.token_counter.token_counter:> [query] Total embedding token usage: 12 tokens


Some of the biggest risk factors in 2020 include:

1. Security breaches that could expose us to liability under various laws and regulations across jurisdictions and increase the risk of litigation and governmental investigation.

2. Degradation of services or sabotage of systems that our security measures may not detect.

3. Individuals able to circumvent our security measures may misappropriate confidential, proprietary, or personal information held by or on behalf of us, disrupt our operations, damage our computers, or otherwise damage our business.

4. Potential failure to attract and retain Drivers and customers.

5. Potential failure to maintain and expand our brand.

6. Potential failure to protect our intellectual property.

7. Potential failure to comply with applicable laws and regulations.

8. Potential failure to manage our growth effectively.

9. High competition in the mobility, delivery, and logistics industries, with competitors in nearly every major geographic region.

10. Lowering of fares or service fees to remain competitive in certain markets, which we have in the past done and may continue to do.

11. Unresolved Staff Comments.

12. Potential failure to comply with applicable laws and regulations related to properties.

13.
INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total LLM token usage: 0 tokens
INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total embedding token usage: 0 tokens

The current risk factors for 2021 include the COVID-19 pandemic and the impact of actions to mitigate the pandemic, the potential for Drivers to be classified as employees, workers or quasi-employees instead of independent contractors, the highly competitive mobility, delivery, and logistics industries, and the need to lower fares or service fees and offer Driver incentives and consumer discounts and promotions in order to remain competitive in certain markets. 

The risk factors for 2020 are outlined in Item 1A of the context information. These risk factors include unresolved staff comments, properties, legal proceedings, and mine safety disclosures. 

The current risk factors as of December 31, 2019 include interest rate risk, investment risk, and foreign currency risk. Interest rate risk relates to the 2016 Term Loan Facility and 2018 Term Loan Facility, which are floating rate notes and are carried at amortized cost. Investment risk is related to cash and cash equivalents including restricted cash and cash equivalents, which totaled $8.2 billion and $12.1 billion as of December 31, 2018 and 2019, respectively. Marketable debt securities classified as short-term investments totaled $440 million as of December 31, 2019. 

Compared to prior years, the risk factors have not changed significantly in 2021, though the impact of the COVID-19 pandemic has been more pronounced. In 2020, the risk factors included unresolved staff comments, properties, legal proceedings, and mine safety disclosures. In 2019, the risk factors included interest rate risk, investment risk, and foreign currency risk. Compared to December 31, 2018, the amount of cash and cash equivalents including restricted cash and cash equivalents has increased from $8.2 billion to $12.1 billion, and the amount of marketable debt securities classified as short-term investments has increased from $0 to $440 million.
> Source (Doc id: 97c61052-ad2a-44eb-a303-9e2417d68168): 
The current risk factors for 2022 include: Drivers being classified as employees, workers or qua...

> Source (Doc id: 828e8b3c-7deb-4228-b936-90bc5a8ea5d8): 
The year provided in the context is 2021. The current risk factors include the COVID-19 pandemic...

> Source (Doc id: 7cd56a0d-eba5-4a0c-a0b6-6ac53969288c): 
The risk factors for 2020 are outlined in Item 1A of the context information. These risk factors...

> Source (Doc id: 03bedde6-bb8d-45fa-baf0-df44aea94499): 
The current risk factors as of December 31, 2019 include interest rate risk, investment risk, an...

> Source (Doc id: f5a4575c-18ba-42f0-9226-67272cd854a2): year: 2022

and certain events we participate in or host with members of the investment community...

> Source (Doc id: 7132cbfe-e484-42f8-a86c-060eca0c8784): year: 2021

into this report or in any other report or document we file.

ITEM 1A. RISK FACTORS

...

> Source (Doc id: 33833b9d-c6cc-4113-b244-e9985d0ca6de): year: 2020

1A.

Risk Factors

11

Item 1B.

Unresolved Staff Comments

46

Item 2.

Properties

...

> Source (Doc id: a0730a98-0816-4d36-9d44-d940e4c05ace): year: 2019

Pronouncements

See

Note 1 - Description of Business and Summary of Significant Acco...
INFO:llama_index.token_counter.token_counter:> [query] Total LLM token usage: 945 tokens
INFO:llama_index.token_counter.token_counter:> [query] Total embedding token usage: 60 tokens
INFO:llama_index.token_counter.token_counter:> [query] Total LLM token usage: 5001 tokens
INFO:llama_index.token_counter.token_counter:> [query] Total embedding token usage: 60 tokens
```