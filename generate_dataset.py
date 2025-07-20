import os
import json
import csv

DATASET_DIR = "C:/Users/Admin/Desktop/smartbugs-curated/dataset"
OUTPUT_CSV = "C:/Users/Admin/Desktop/ChainSage/dataset/chain_sage_dataset.csv"

def is_vulnerable(filepath):
    """Return 1 if file has known vulnerability annotations."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        return '@vulnerable_at_lines' in content

def collect_contracts():
    rows = []
    for category in os.listdir(DATASET_DIR):
        category_path = os.path.join(DATASET_DIR, category)
        if not os.path.isdir(category_path):
            continue

        for filename in os.listdir(category_path):
            if filename.endswith('.sol'):
                file_path = os.path.join(category_path, filename)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    code = f.read().replace('\n', ' ')  # flatten code
                    label = 1 if is_vulnerable(file_path) else 0
                    rows.append([code, label])
    return rows

def save_to_csv(rows):
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
    with open(OUTPUT_CSV, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['code', 'label'])
        writer.writerows(rows)

if __name__ == "__main__":
    print("📥 Collecting contracts...")
    data = collect_contracts()
    print(f"✅ Total contracts found: {len(data)}")
    print("💾 Saving dataset CSV...")
    save_to_csv(data)
    print(f"✅ Saved to: {OUTPUT_CSV}")
