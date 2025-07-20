from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load tokenizer from the original base model
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")

# Load your fine-tuned model from local path
model = AutoModelForSequenceClassification.from_pretrained("models/codebert_classifier").to("cuda")

# Example code snippet to classify
code = """function withdraw(uint amount) public {
    require(balance[msg.sender] >= amount);
    msg.sender.call{value: amount}(""); // re-entrancy risk
    balance[msg.sender] -= amount;
}"""

# Tokenize and move to GPU
inputs = tokenizer(code, return_tensors="pt", truncation=True, padding=True).to("cuda")

# Inference
with torch.no_grad():
    outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1).item()

# Print result
try:
    print("Prediction:", "🛑 Vulnerable" if prediction == 1 else "✅ Safe")
except UnicodeEncodeError:
    print("Prediction:", "VULNERABLE" if prediction == 1 else "SAFE")
