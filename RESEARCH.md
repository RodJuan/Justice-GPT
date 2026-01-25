# Research: AI Models for False Confession Detection

To implement Phase 2 of the Roadmap, we are evaluating the following models from Hugging Face for linguistic and psychological pattern analysis:

## Recommended Models (NLP/BERT)
1. **Legal-BERT:** Specifically pre-trained on legal corpora (contracts, cases, and litigation). Ideal for understanding the context of legal language in confessions.
2. **RoBERTa-large-mnli:** Excellent for Natural Language Inference (NLI). It can help detect contradictions between a suspect's statement and known facts.
3. **Sentiment Analysis Transformers:** To detect emotional spikes or "scripted" lack of emotion in coerced statements.

## Data Sources for Fine-Tuning
- **Innocence Project Case Archives:** For verified wrongful conviction narratives.
- **Linguistic Corpuses:** Focused on coerced vs. voluntary speech patterns.

## Goal
The 'Psych Layer' will use these models to flag statements with a high "Coercion Probability Index."


## Data Sourcing & Bias Mitigation

Exoneration Registry Data: The National Registry of Exonerations offers a goldmine of public summaries on proven wrongful convictions, including breakdowns of false confessions (which factor into about 13% of their 3,608 tracked exonerations as of 2024). 

pmc.ncbi.nlm.nih.gov

We can scrape or download their case database (available via CSV exports on their site) for anonymized summaries of coerced statements—e.g., filtering for cases involving official misconduct or perjury, which overlap heavily with false confessions in homicide exonerations. 

deathpenaltyinfo.org 

This gives us hundreds of labeled examples (e.g., "false confession" tagged cases) to bootstrap training, all in the public domain. I'll draft a Python scraper in /psych-layer/data_pull.py to fetch and anonymize these ethically.
FOIA Requests for Public Domain Transcripts: Spot on for deeper, verbatim material. While direct transcripts aren't always hosted online, FOIA has unlocked many wrongful conviction records—think declassified interrogation logs from high-profile exonerations via the Innocence Project's resources or DOJ archives. 

innocenceproject.org 

To start, we can target aggregated public releases (e.g., from the Reporters Committee for Freedom of the Press or OJP sites) without filing new requests, ensuring we're pulling from already-disclosed sources to sidestep delays. 

rcfp.org 

This'll enrich our dataset with regional dialects from U.S. cases, like those in urban vs. rural jurisdictions.
Synthetic Benchmarking: For bias audits without real victim exposure, synthetic data is our ethical powerhouse. We can generate diverse "ground truth" datasets simulating legal texts across dialects (e.g., AAVE, Southern U.S., immigrant-influenced English) using LLMs, then audit with frameworks like those in recent papers on de-biasing legal language models. 

researchgate.net 

Tools like AIF360 can quantify disparities, and datasets like LexGLUE (a benchmark for legal NLP) provide a starting point for fine-tuning on unbiased legal understanding. 

eprints.whiterose.ac.uk 

Let's aim for 1,000 synthetic samples initially, varied by socioeconomic factors, to test and mitigate any cultural misreads as coercion.

