from app import API_URL
import requests
import streamlit as st

st.header("🗒️ Lista de Tasks")
try:
    tasks = requests.get(f"{API_URL}/tasks/").json()
    st.table(tasks)
except Exception as e:
    st.error(f"Erro ao buscar tasks: {e}")
