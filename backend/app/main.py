from fastapi import FastAPI

from app.api import router as api_router

app = FastAPI(
    title="API m00",
    description="Backend principal do projeto m00",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"msg": "API rodando com sucesso"}

app.include_router(api_router)
