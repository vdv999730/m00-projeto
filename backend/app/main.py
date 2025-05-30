from fastapi import FastAPI
from app.api import auth, tasks

app = FastAPI(title="m00-backend")

# 1. Rota raiz de boas-vindas
@app.get("/", tags=["root"])
async def read_root():
    return {"message": "API Backend Online 🚀"}

# 2. Rotas de Tasks
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])

# 3. Rotas de Auth
app.include_router(auth.router, prefix="/auth", tags=["auth"])
