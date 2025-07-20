import pandas as pd
import torch
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# === Load fine-tuned model and tokenizer ===
model_path = "models/codebert_classifier"
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")  # Use base tokenizer
model = AutoModelForSequenceClassification.from_pretrained(model_path).to("cuda")
model.eval()

# === Load CSV test data ===
csv_path = r"C:\Users\Admin\Desktop\ChainSage\dataset\chain_sage_dataset.csv"
df = pd.read_csv(csv_path)
codes = df["code"].tolist()
true_labels = df["label"].tolist()

# === Prediction Loop ===
predictions = []
results = []

for i, (code, true_label) in enumerate(tqdm(zip(codes, true_labels), total=len(df), desc="🔍 Evaluating")):
    try:
        inputs = tokenizer(code, return_tensors="pt", truncation=True, padding=True).to("cuda")
        with torch.no_grad():
            outputs = model(**inputs)
        pred_label = torch.argmax(outputs.logits, dim=1).item()
        predictions.append(pred_label)
        results.append("✅" if pred_label == true_label else "❌")
        print(f"[{results[-1]}] Row {i+1}: Pred → {'Vulnerable' if pred_label else 'Safe'} | Actual → {'Vulnerable' if true_label else 'Safe'}")

    except Exception as e:
        print(f"❌ Error at row {i+1}: {e}")
        predictions.append(-1)
        results.append("❌")

# === Filter out any failed predictions (-1) ===
df["prediction"] = predictions
df["result"] = results
valid_df = df[df["prediction"] != -1]

# === Save Results CSV ===
output_csv = r"C:\Users\Admin\Desktop\ChainSage\dataset\prediction_results.csv"
df.to_csv(output_csv, index=False)
print(f"\n📁 Saved prediction results to: {output_csv}")

# === Accuracy & F1 Score (on valid predictions only) ===
y_true = valid_df["label"].tolist()
y_pred = valid_df["prediction"].tolist()

acc = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print(f"\n📊 Accuracy: {acc * 100:.2f}%")
print(f"🎯 F1 Score: {f1:.4f}")

# === Classification Report ===
print("\n🔎 Classification Report:")
print(classification_report(y_true, y_pred, target_names=["Safe", "Vulnerable"]))

# === Confusion Matrix ===
cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=["Safe", "Vulnerable"],
            yticklabels=["Safe", "Vulnerable"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.tight_layout()

# === Save Confusion Matrix Image ===
conf_matrix_path = r"C:\Users\Admin\Desktop\ChainSage\dataset\confusion_matrix.png"
plt.savefig(conf_matrix_path)
print(f"📸 Saved confusion matrix to: {conf_matrix_path}")
plt.show()
