import os

API_URL = os.getenv("API_URL", "https://backend-d4gi.onrender.com")

import requests
import streamlit as st

st.header("🗒️ Lista de Tasks")
try:
    tasks = requests.get(f"{API_URL}/tasks/").json()
    st.table(tasks)
except Exception as e:
    st.error(f"Erro ao buscar tasks: {e}")
