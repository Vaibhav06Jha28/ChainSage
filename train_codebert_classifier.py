import transformers
print("Transformers version:", transformers.__version__)

from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer, AutoTokenizer
from datasets import load_dataset
import torch
import pandas as pd
from sklearn.model_selection import train_test_split

# Load CSV dataset
df = pd.read_csv("dataset/chain_sage_dataset.csv")

# Prepare dataset
train_texts, val_texts, train_labels, val_labels = train_test_split(df['code'], df['label'], test_size=0.2)

# Load tokenizer and encode
model_name = "microsoft/codebert-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)

train_encodings = tokenizer(list(train_texts), truncation=True, padding=True)
val_encodings = tokenizer(list(val_texts), truncation=True, padding=True)

class ContractDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        return {
            **{k: torch.tensor(v[idx]) for k, v in self.encodings.items()},
            "labels": torch.tensor(self.labels[idx])
        }

    def __len__(self):
        return len(self.labels)

train_dataset = ContractDataset(train_encodings, list(train_labels))
val_dataset = ContractDataset(val_encodings, list(val_labels))

# Define model
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

print("Using device:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU")


# Training args
training_args = TrainingArguments(
    output_dir="models/codebert_classifier",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    save_total_limit=1,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    push_to_hub=False,
    save_safetensors=True,  # ✅ This avoids torch.load issue
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
)

trainer.train()
