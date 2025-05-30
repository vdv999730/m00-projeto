from fastapi import FastAPI
from app.api import auth  # Corrigir se o path for diferente

app = FastAPI(
    title="M00 Projeto API",
    description="API Backend Online 🚀",
    version="1.0.0"
)

#app.include_router(auth.router)
#app.include_router(auth.router)  # ← sem prefixo
#app.include_router(auth.router, tags=["Auth"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])  # <-- ESSENCIAL


@app.get("/")
def read_root():
    return {"message": "API Backend Online 🚀"}
