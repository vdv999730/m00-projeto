from fastapi import FastAPI
from api import auth  # Corrigir se o path for diferente

app = FastAPI(
    title="M00 Projeto API",
    description="API Backend Online 🚀",
    version="1.0.0"
)

#app.include_router(auth.router)
app.include_router(auth.router)  # ← sem prefixo

@app.get("/")
def read_root():
    return {"message": "API Backend Online 🚀"}
