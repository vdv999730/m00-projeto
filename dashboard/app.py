import streamlit as st

st.set_page_config(page_title="Dashboard m00", page_icon="🧠")

st.title("🧠 Dashboard m00")
st.sidebar.title("Menu")

st.sidebar.subheader("Navegação")
page = st.sidebar.selectbox("Selecione a página", ["Home", "Monitoramento", "WhatsApp", "Status API"])

if page == "Home":
    st.subheader("Bem-vindo ao Dashboard m00")
elif page == "Monitoramento":
    st.subheader("Monitoramento do Banco de Dados")
elif page == "WhatsApp":
    st.subheader("Status do WhatsApp")
elif page == "Status API":
    st.subheader("Status da API Backend")
