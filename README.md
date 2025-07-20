
# 🔐 ChainSage – AI-Powered Smart Contract Vulnerability Analyzer

**ChainSage** is an advanced AI-based security analyzer that detects, explains, and visualizes vulnerabilities in Ethereum-based Solidity smart contracts. Powered by a fusion of deep learning (CodeBERT, Mistral), anomaly detection (Isolation Forest), and rule-based logic, ChainSage offers a seamless DevSecOps solution through its powerful FastAPI backend and modern Streamlit UI.

---

## 📖 Introduction

**ChainSage** is an advanced AI-driven auditing tool designed to analyze and secure Ethereum smart contracts written in Solidity. It seamlessly integrates **Machine Learning**, **Rule-Based Engines**, and **Visual Analysis** to identify, explain, and visualize security vulnerabilities with high accuracy and contextual relevance.

This tool is ideal for:

- 🛠️ Blockchain developers  
- 🔐 Web3 auditors  
- 🧠 Security researchers  
- 📘 Smart contract learners  

![Dashboard Screenshot](./assets/Dashboard/dashboard1.png)

---

## 🚀 Features

- 🤖 **AI-Powered Detection Engine**
  - Uses **CodeBERT** (fine-tuned on Solidity contracts) and **Mistral** for advanced contextual analysis
  - Identifies logical vulnerabilities like `Reentrancy`, `tx.origin misuse`, and more

- 🔍 **Hybrid Rule-Based Enhancements**
  - Custom detection for `.call()`, `unchecked-send`, and unprotected ownership transfer
  - Works alongside the ML models to increase reliability and precision

- 📊 **Dynamic Risk Diagrams with Graphviz**
  - Converts control flow into **visual threat maps**
  - Clearly highlights critical paths and exploitable entry points

- 🧠 **Streamlit-Powered Dashboard**
  - Upload Solidity `.sol` contracts for instant analysis
  - Displays AI-generated HTML reports and SVG graphs

- 🔐 **Secure Coding Recommendations**
  - Suggestions inspired by **OpenZeppelin**, **ConsenSys**, and **Slither** audits
  - Actionable prevention tips integrated into every finding

- ⚙️ **FastAPI & CLI Integration**
  - RESTful API for remote ML inference and contract analysis
  - Run directly via command-line or hook into CI/CD pipelines

- 🧪 **Included Vulnerable Contracts**
  - Sample `.sol` contracts with known issues for testing and demoing
  - Great for education, debugging, and benchmarking

---

## 🧠 AI & Detection Models Used

| Model                  | Role                                                              |
|------------------------|-------------------------------------------------------------------|
| 🧠 **CodeBERT**         | Transformer model fine-tuned to classify Solidity snippets        |
| 🔎 **Mistral-7B**       | Explains detected issues in natural language (via prompting)      |
| 🌲 **Isolation Forest** | Detects outliers in contract structure/statistics                 |
| ⚠️ **Rule Engine**      | Uses RegEx and patterns to detect risky Solidity behaviors        |

---

## 🧱 Architecture & Workflow

```mermaid
graph TD
    A[User Uploads .sol File] --> B[Streamlit UI]
    B --> C[FastAPI Backend]
    C --> D[CodeBERT Classifier]
    C --> E[Mistral Explainer]
    C --> F[Rule-Based Analyzer]
    C --> G[Graphviz SVG Generator]
    G --> H[Visual Report]
    E --> H
    D --> H
    F --> H
    H --> I[HTML Vulnerability Report + Diagram]

---
## 🛠️ Tech Stack


=======
![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)
![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-orange)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)
![Graphviz](https://img.shields.io/badge/Visualization-Graphviz-blue)
![PyTorch](https://img.shields.io/badge/ML-PyTorch-red)
![HuggingFace](https://img.shields.io/badge/Transformers-HuggingFace-yellow)

**Components:**
- **Frontend**: Streamlit + Lottie + Custom HTML/CSS
- **Backend**: FastAPI + PyTorch + Transformers + Graphviz
- **ML Models**: CodeBERT, Mistral (via API), Isolation Forest

---
### 📊 Dashboard View
![Dashboard Screenshot](./assets/Dashboard/dashboard1.png)

### 📩 Response Example
![Response Screenshot](./assets/Response/response1.png)
![Response Screenshot](./assets/Response/response2.png)

### 🖼️ UI Screenshot
![UI Screenshot](./assets/UI/UI.png)


=======
---
## 📂 Project Structure

```
ChainSage/
├── api/
│   └── routes/
│       └── vulnerability.py    ← FastAPI route for model-based vulnerability detection
├── ai_models/
│   └── vulnerability_detector.py
├── models/
│   └── codebert_classifier/    ← Fine-tuned CodeBERT model
│   └── isolation_forest.pkl
│   └── ppo_wallet.zip
├── smart_contracts/
│   └── sample_contracts/
│       └── vulnerable_contract.sol
├── frontend/
│   └── streamlit_app/
│       └── app.py              ← Streamlit frontend UI
├── test_contract.sol
├── mistral_vulnerability_checker.py
├── generate_dataset.py
├── evaluate_model.py
├── train_codebert_classifier.py
├── cli_infer.py
├── .env
├── requirements.txt
└── README.md                  ← You're here!
```
## ▶️ Getting Started

```bash
# Clone the repository
git clone https://github.com/Vaibhav06Jha28/ChainSage.git
cd ChainSage

# Setup Python virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Start backend API
cd api
uvicorn main:app --reload

# Launch Streamlit frontend

cd ../frontend/streamlit_app
streamlit run app.py
```


=======
> ⚠️ **Important**: Install Graphviz and ensure `dot` is available in system PATH.

---

## 📉 Sample Report Output

- **Type**: Reentrancy Attack
- **Detected By**: CodeBERT + Rule Engine
- **Severity**: 🔴 High
- **Explanation**: External call before state update
- **Fix**: Apply Checks-Effects-Interactions pattern or use `ReentrancyGuard`


---

## 👨‍💻 Made By



**Vaibhav Jha**  
🔗 [LinkedIn](https://www.linkedin.com/in/vaibhav-jha-27191b1ba/)  
🧑‍💻 [GitHub](https://github.com/Vaibhav06Jha28)

---

## 📜 License

MIT License © 2025 Vaibhav Jha

---

