import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "https://backend-d4gi.onrender.com")

st.title("🔗 Status da API Backend")

# 1. Check raiz
try:
    resp_root = requests.get(API_URL)
    if resp_root.status_code == 200:
        st.success(f"✅ API Online: {resp_root.json()['message']}")
    else:
        st.error(f"❌ API Offline - Status {resp_root.status_code}")
except Exception as e:
    st.error(f"Erro de conexão na raiz: {e}")

# 2. Check versão
try:
    resp_ver = requests.get(f"{API_URL}/auth/version")
    if resp_ver.status_code == 200:
        data = resp_ver.json()
        st.info(f"• Versão: {data['version']}\n• Sistema: {data['system']}")
    else:
        st.warning(f"⚠️ /auth/version retornou {resp_ver.status_code}")
except Exception as e:
    st.error(f"Erro de conexão em /auth/version: {e}")
