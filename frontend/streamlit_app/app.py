import streamlit as st
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load the Lottie animation once at the top
lottie_ai = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_1pxqjqps.json")

st.set_page_config(page_title="ChainSage", layout="wide")
st.title("🔐 ChainSage - Blockchain AI Security Dashboard")

st.sidebar.header("📄 Upload Smart Contract")
uploaded_file = st.sidebar.file_uploader("Upload Solidity File (.sol)", type=["sol"])

if uploaded_file:
    contract_code = uploaded_file.read().decode("utf-8")
    st.subheader("📜 Smart Contract Preview")
    st.code(contract_code, language="solidity")

    if st.button("🔍 Analyze for Vulnerabilities"):
        with st.spinner("Analyzing using Mistral + CodeBERT..."):
            try:
                response = requests.post(
                    "http://localhost:8000/vulnerability/analyze",
                    json={"code": contract_code},
                    timeout=30
                )
                response.raise_for_status()
                report_html = response.text

                if "Vulnerability Detected" in report_html:
                    st.error("⚠️ Vulnerabilities Found!")
                else:
                    st.success("✅ Smart contract is safe.\n\n🔒 No critical vulnerabilities detected.")

                st.subheader("🧠 AI-Powered Vulnerability Report")
                components.html(report_html, height=1000, scrolling=True)

            except requests.exceptions.RequestException as e:
                st.error(f"❌ API Error: {e}")
else:
    # 🎥 Show Lottie animation if no file is uploaded
    st_lottie(lottie_ai, height=300, key="intro")

    st.markdown("""
        <div style='text-align: center;'>
            <h2 style='color:#4CAF50;'>Welcome to ChainSage</h2>
            <p>🔍 Upload a Solidity contract to detect vulnerabilities using AI</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown(
    "<hr><small style='color:gray;'>Built with FastAPI & Streamlit – ChainSage Project © 2025</small>",
    unsafe_allow_html=True
)
