import streamlit as st
import requests

st.title("🔗 Status da API Backend")

api_url = "https://backend-d4gi.onrender.com"

try:
    response = requests.get(api_url)
    if response.status_code == 200:
        st.success(f"✅ API Online: {response.json()}")
    else:
        st.error(f"❌ API Offline - Status Code: {response.status_code}")
except Exception as e:
    st.error(f"Erro de conexão: {e}")
