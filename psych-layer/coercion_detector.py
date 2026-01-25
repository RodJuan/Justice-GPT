import torch
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

# Load dataset (e.g., from Hugging Face or local CSV)
dataset = load_dataset('csv', data_files='coercion_dataset.csv')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def preprocess(examples):
    return tokenizer(examples['statement'], truncation=True, padding=True)

tokenized_dataset = dataset.map(preprocess, batched=True)

# Model setup
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# Training args
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    evaluation_strategy='epoch'
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset['train'],
    eval_dataset=tokenized_dataset['test']
)

trainer.train()

# Inference example
text = "Sample confession text here"
inputs = tokenizer(text, return_tensors='pt')
outputs = model(**inputs)
prediction = torch.argmax(outputs.logits, dim=1).item()  # 0: non-coerced, 1: coerced
