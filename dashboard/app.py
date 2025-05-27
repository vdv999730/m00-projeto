import streamlit as st

st.set_page_config(page_title="Dashboard m00", layout="wide")

st.title("📊 Dashboard m00")
st.subheader("Painel principal operacional")
st.markdown("---")

menu = ["Home", "Status API", "Monitor DB", "WhatsApp"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.info("Seja bem-vindo ao Dashboard m00!")

elif choice == "Status API":
    st.write("Verificar status das APIs...")

elif choice == "Monitor DB":
    st.write("Visualização da base de dados...")

elif choice == "WhatsApp":
    st.write("Gerenciamento do WhatsApp...")

st.sidebar.markdown("---")
st.sidebar.caption("Projeto m00 - 2025")
