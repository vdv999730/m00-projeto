from fastapi import FastAPI
from api import auth

# 🚀 Inicializa a aplicação
app = FastAPI()

# 🔗 Inclui as rotas de autenticação
app.include_router(auth.router)

# 🌎 Endpoint raiz → Teste rápido
@app.get("/")
def read_root():
    return {"message": "API Backend Online 🚀"}
