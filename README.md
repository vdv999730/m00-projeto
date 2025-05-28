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
1️⃣ Tenha o arquivo render.yaml na raiz.

2️⃣ Acesse https://render.com → New → Blueprint Deploy.

3️⃣ Insere o link do seu repositório GitHub.

4️⃣ O Render detecta e sobe:

✅ Backend

✅ Dashboard

✅ Banco PostgreSQL

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
