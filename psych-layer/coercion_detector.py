import torch
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

# 1. Load the local synthetic dataset
# Make sure coercion_dataset.csv is inside the /data folder
dataset = load_dataset('csv', data_files='data/coercion_dataset.csv')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def preprocess(examples):
    """Tokenizes the input text for BERT processing."""
    return tokenizer(examples['statement'], truncation=True, padding=True)

# 2. Dataset Processing
tokenized_dataset = dataset.map(preprocess, batched=True)

# Split the 30 examples into Training (80%) and Testing (20%)
# This ensures the model can evaluate its own performance
tokenized_dataset = tokenized_dataset['train'].train_test_split(test_size=0.2)

# 3. Model Initialization
# Using 'bert-base-uncased' as the foundational brain for text classification
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# 4. Training Configuration
training_args = TrainingArguments(
    output_dir='./results',          # Output directory for model checkpoints
    num_train_epochs=3,              # Number of training passes
    per_device_train_batch_size=8,   # Batch size for training
    per_device_eval_batch_size=8,    # Batch size for evaluation
    warmup_steps=10,                 # Linear warmup over training steps
    weight_decay=0.01,               # Regularization to prevent overfitting
    logging_dir='./logs',            # Directory for storing logs
    eval_strategy='epoch'            # Evaluate the model at the end of each epoch
)

# 5. Training Execution
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset['train'],
    eval_dataset=tokenized_dataset['test']
)

print("Starting training process...")
trainer.train()

# 6. Final Inference Test
def predict_coercion(text):
    """
    Takes a string and returns the probability of coercion.
    0: Genuine Statement
    1: Coerced/False Confession
    """
    inputs = tokenizer(text, return_tensors='pt')
    outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1).item()
    return "COERCION DETECTED" if prediction == 1 else "GENUINE STATEMENT"

# Real-world test case (Coercive pattern)
test_text = "I don't remember the details clearly, but the detective said I was there, so I guess it must be true."
result = predict_coercion(test_text)
print(f"\n--- Inference Test ---")
print(f"Input: {test_text}")
print(f"Result: {result}")
