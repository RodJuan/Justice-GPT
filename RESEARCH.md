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
