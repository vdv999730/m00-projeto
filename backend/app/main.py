from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API Backend m00",
    description="Backend desenvolvido em FastAPI",
    version="1.0.0",
)

# Configuração de CORS (opcional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importar rotas aqui
# from app.api import router as api_router
# app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "API m00 funcionando corretamente 🚀"}
