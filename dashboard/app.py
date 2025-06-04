import os

API_URL = os.getenv("API_URL", "https://backend-d4gi.onrender.com")

import streamlit as st

st.set_page_config(page_title="Dashboard m00", layout="wide")

st.title("📊 Dashboard m00 - Painel Principal")
st.markdown("### Bem-vindo ao Dashboard de Monitoramento e Controles 🚀")

st.info("Escolha uma opção no menu lateral para navegar entre as páginas.")
