# 🚀 Backend - Projeto m00

Este é o backend (API) do projeto **m00**, desenvolvido com **FastAPI**, configurado para deploy no **Render**.

---

## 📚 Tecnologias
- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL (Render Database)
- Docker (para deploy)
- Pytest (para testes)
- Pydantic

---

## 🚀 Como rodar localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd backend

2. Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


3. Instalar dependências
pip install -r requirements.txt


4. Configurar variáveis de ambiente
Crie um arquivo .env baseado no .env.example:
cp .env.example .env

Edite o .env com seus dados:
DATABASE_URL=postgresql+asyncpg://<user>:<password>@<host>/<database>
SECRET_KEY=sua-secret-key-aqui
ALGORITHM=HS256
ENVIRONMENT=production


5. Rodar a aplicação
uvicorn app.main:app --reload

Acesse a documentação Swagger em:
http://localhost:8000/docs


🐳 Deploy no Render
O deploy está configurado via Docker:

O Dockerfile já está pronto.

O serviço é buildado a cada push na branch main.

Configurações importantes no Render:

Variáveis de Ambiente: DATABASE_URL, SECRET_KEY, ALGORITHM, ENVIRONMENT

Health Check: /docs

Deploy automático: Ativado
🧪 Rodar testes
pytest

📦 Estrutura do projeto
backend/
├── app/
│   ├── main.py
│   ├── api/
│   ├── core/
│   └── models/
├── tests/
├── .env.example
├── requirements.txt
├── Dockerfile



---

## 📄 `dashboard/README.md`
```markdown
# 📊 Dashboard - Projeto m00

Este é o painel visual (dashboard) do projeto **m00**, que consome dados da API backend.

---

## 📚 Tecnologias
- Python 3.11
- Streamlit
- Docker (para deploy)
- Requests

---

## 🚀 Como rodar localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd dashboard

2. Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Instalar dependências
pip install -r requirements.txt


4. Configurar variáveis de ambiente
Crie um arquivo .env baseado no .env.example:
copy .env.example .env   # No Windows
# ou
cp .env.example .env     # No Linux/Mac


Edite o .env:
API_URL=https://backend-d4gi.onrender.com


5. Rodar o dashboard
streamlit run app.py


Acesse localmente em:
http://localhost:8501


🐳 Deploy no Render
Deploy configurado via Docker.

Health Check: /

Variável de Ambiente: API_URL=https://backend-d4gi.onrender.com


📦 Estrutura do projeto
dashboard/
├── app.py
├── pages/
│   ├── dashboard_graficos.py
│   └── status_api.py
├── .env.example
├── requirements.txt
├── Dockerfile


