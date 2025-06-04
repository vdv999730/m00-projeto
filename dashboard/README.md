# 📊 Dashboard - Projeto m00

Este é o painel visual (dashboard) do projeto **m00**, conectado à API backend em FastAPI.

---

## 🚀 Instruções de Uso

### 1. Instalar dependências

Certifique-se de ter o Python 3.11 instalado.  
Crie e ative seu ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt


2. Variáveis de Ambiente
Crie um arquivo .env com base no .env.example existente:
cp .env.example .env


Edite o arquivo .env com a URL da API:
API_URL=https://backend-d4gi.onrender.com


3. Rodar o dashboard localmente
streamlit run app.py


Ou, se estiver em pages/:
streamlit run pages/dashboard_graficos.py



🐳 Deploy
O deploy do dashboard está configurado via Docker e Render.

URL de produção:
https://dashboard-oqd1.onrender.com

Variáveis no Render:

API_URL=https://backend-d4gi.onrender.com


📁 Estrutura esperada
dashboard/
├── app.py
├── pages/
│   ├── dashboard_graficos.py
│   └── status_api.py
├── .env.example
├── requirements.txt
├── Dockerfile



✅ Checklist de Boas Práticas
 .env está no .gitignore

 .env.example está versionado

 Deploy automático ativo via Render

 Healthcheck configurado