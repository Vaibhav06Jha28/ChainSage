# 🔐 ChainSage – AI-Powered Smart Contract Vulnerability Analyzer

**ChainSage** is a cutting-edge AI-driven security toolkit that detects and explains vulnerabilities in Ethereum-based Solidity smart contracts. It leverages CodeBERT, Mistral, Isolation Forest, and custom rule-based detection, and presents results via a modern FastAPI backend and a Streamlit frontend dashboard – complete with live diagram generation using Graphviz.


![Dashboard Screenshot](./assets/Dashboard/dashboard1.png)

---



🚀 Why ChainSage Stands Out

💡 AI That Knows Solidity Inside-Out
Trained on thousands of smart contracts, CodeBERT + Mistral detect subtle flaws that static tools miss — even in complex logic flows.

🧠 Hybrid Detection Engine
Combines deep learning with rule-based logic to catch critical vulnerabilities like reentrancy, unchecked .call(), gas griefing, and more.

🎯 Instant Visual Threat Mapping
Transforms vulnerabilities into Graphviz-powered SVG diagrams, highlighting affected functions and severity — like X-rays for your code.

📊 Interactive Streamlit Dashboard
Upload .sol files, click Analyze, and receive a beautiful HTML report, complete with collapsible details, AI explanations, and icons.

🔐 Audit-Ready Insights
Built-in best practices from OpenZeppelin, Slither, and ConsenSys help you not just detect, but harden your contracts.

⚙️ CLI + API for Pros
Audit via terminal or plug directly into CI/CD pipelines using the FastAPI backend. Scalable. Scriptable. Production-ready.

🧪 Battle-Tested on Real Vulnerabilities
Includes a library of vulnerable smart contracts to demo detections and verify model robustness.

🔥 Make Your Contracts Bulletproof
Whether you're shipping to mainnet or presenting to investors — ChainSage lets you audit, understand, and secure your smart contracts like a pro.





---
![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)
![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-orange)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)

---
## 🖼 Sample UI

| Vulnerability Report | AI-Generated Risk Graph |
|----------------------|-------------------------|
|![Response Screenshot](./assets/Response/response1.png)  | ![Response Screenshot](./assets/Response/response2.png) |

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit + HTML components + Lottie animations
- **Backend**: FastAPI + PyTorch + HuggingFace Transformers
- **Model**: CodeBERT fine-tuned on Solidity contracts
- **Visualization**: Graphviz (risk graph), Markdown (explanations)

---


### 📊 Dashboard View
![Dashboard Screenshot](./assets/Dashboard/dashboard1.png)

### 📩 Response Example
![Response Screenshot](./assets/Response/response1.png)
![Response Screenshot](./assets/Response/response2.png)

### 🖼️ UI Screenshot
![UI Screenshot](./assets/UI/UI.png)



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




## ▶️ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/Vaibhav06Jha28/ChainSage.git
cd ChainSage

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start backend (FastAPI)
cd api
uvicorn main:app --reload

# 5. Start frontend (Streamlit)
cd ../frontend/streamlit_app
streamlit run app.py
```

---

## ⚠️ Notes
- Ensure **Graphviz is installed** and `dot` is available in PATH.
- Backend runs at `http://localhost:8000/vulnerability/analyze`
- Make sure both Streamlit and FastAPI servers are running.

---

## 📉 Example Output

- Vulnerability Type: Reentrancy
- Risk Level: High
- Reason: External call before internal state update
- Recommendation: Use Checks-Effects-Interactions / ReentrancyGuard
- Dynamic Diagram: ✅ Auto-generated via Graphviz

---
## 📜 License

MIT License © 2025 Vaibhav Jha

---

## 👨‍💻 Made By

- **Vaibhav Jha**  
  🔗 [LinkedIn](https://www.linkedin.com/in/vaibhav-jha-27191b1ba/)  
  🧑‍💻 [GitHub](https://github.com/Vaibhav06Jha28)
