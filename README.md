🧠 README – m00-projeto
🚀 Visão Geral
m00-projeto é uma infraestrutura backend + dashboard + banco, escalável, baseada em Python (FastAPI), Streamlit (ou outro frontend) e PostgreSQL.

→ 🔥 Totalmente dockerizado.
→ 🔥 Deploy automático via Render.
→ 🔥 Pronto para desenvolvimento, produção e escalabilidade.

🗂️ Estrutura do Projeto
plaintext
Copiar
Editar
m00-projeto/
├── backend/
│   ├── app/
│   ├── Dockerfile
│   ├── requirements.txt
├── dashboard/
│   ├── pages/
│   ├── Dockerfile
│   ├── requirements.txt
├── db-model/
│   ├── diagram.md
│   ├── estrutura.sql
├── docs/
│   ├── arquitetura.md
│   ├── setup.md
├── docker-compose.yml (opcional)
├── render.yaml (deploy automático no Render)
├── README.md
⚙️ Requisitos
Docker e Docker Compose instalados ✔️
ou

Python 3.12+ ✔️

🐳 Rodando Local com Docker Compose (FULL STACK)
bash
Copiar
Editar
docker-compose up --build
→ Isso sobe:

Backend em http://localhost:10000

Dashboard em http://localhost:8501 (ou porta configurada)

PostgreSQL interno na porta 5432

🔧 Rodando Backend Local (Manual)
▶️ Ambiente Virtual (sem Docker):
bash
Copiar
Editar
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 10000 --reload
→ Acessa em: http://localhost:10000/docs

🔧 Rodando Dashboard Local (Manual)
▶️ Streamlit exemplo:
bash
Copiar
Editar
cd dashboard
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
→ Acessa em: http://localhost:8501

☁️ Deploy no Render (Blueprint)
1. **Ajuste o arquivo `render.yaml`**  
   - Garanta que `rootDir` aponte para `backend` e `dashboard`.  
   - Preencha em `envVars` as suas variáveis:
     ```yaml
     services:
       - name: m00-backend
         rootDir: backend
         envVars:
           - key: DATABASE_URL
             value: postgresql://<user>:<password>@<host>:<port>/<dbname>
           - key: SECRET_KEY
             value: <sua_chave_forte>
       - name: m00-dashboard
         rootDir: dashboard
     ```

2. **Commit & Push para o GitHub**  
   ```bash
   git add render.yaml
   git commit -m "🔄 Atualiza deploy no Render"
   git push origin main

3. Configure as Env Vars no painel do Render

	Acesse: https://dashboard.render.com

	Serviços → m00-backend → Environment
	
		# Database
	DATABASE_URL=value: postgresql://matrix_db_2qsn_user:4vwvRr2W8HfEMQ7R78LKUGcKPMCe16lU@dpg-d0q819buibrs73dn90r0-a.oregon-postgres.render.com:5432/matrix_db_2qsn

		# Security
	SECRET_KEY=<4f294976b1a2a6bda9ff8a598609108e246002bf32aa6c8788da008466cc3542>
ALGORITHM=HS256

# Streamlit (opcional)
STREAMLIT_PORT=8501


	Faça o mesmo em m00-dashboard (caso use variáveis).

4. Verifique o build automático

	Depois do push, o Render inicia o build automaticamente.

	Acesse a aba Deploys do serviço e aguarde “Live” ou “Healthy”.

5. Teste em produção
# Backend
curl https://backend-d4gi.onrender.com/
# Dashboard
open https://dashboard-oqd1.onrender.com/

Confirme que o backend retorna {"message":"API Backend Online 🚀"}

Confirme que o dashboard carrega sem erro.


🔐 Variáveis de Ambiente (.env ou Render)
Variável	Descrição
DATABASE_URL	URL do banco PostgreSQL Render
SECRET_KEY	Chave secreta JWT
ALGORITHM	Algoritmo de criptografia (ex: HS256)
PORT	Porta do backend (default: 10000)

🔗 Endpoints Backend (FastAPI)
Docs Swagger → http://localhost:10000/docs

OpenAPI JSON → http://localhost:10000/openapi.json

📜 Comandos Úteis – GIT
Ação	Comando
Checar status	git status
Adicionar tudo	git add .
Commitar	git commit -m "mensagem"
Push	git push
Resolver conflito	git add <arquivo> + git rebase --continue
Cancelar rebase	git rebase --abort

📦 Comandos Úteis – DOCKER
Ação	Comando
Build backend	docker build -t m00-backend ./backend
Run backend	docker run -p 10000:10000 m00-backend
Build dashboard	docker build -t m00-dashboard ./dashboard
Run dashboard	docker run -p 8501:8501 m00-dashboard
Subir tudo com docker-compose	docker-compose up --build

🧠 Observações Importantes
✔️ O render.yaml controla todo o deploy automático na Render.

✔️ Usa docker-compose.yml se quiser rodar tudo local (opcional).

✔️ Usa .env para controle de variáveis sensíveis.

🤖 Autores
🧠 CV + ChatGPT Engenharia Cognitiva Avançada

🏆 Status:
✔️ Operacional
✔️ Deploy automático funcionando
✔️ Pronto para produção e expansão

## Getting Started

### Pré-requisitos
- Docker & Docker Compose
- Git

### Setup local
1. Clone o repositório  
   ```bash
   git clone https://github.com/vdv999730/m00-projeto.git
   cd m00-projeto

