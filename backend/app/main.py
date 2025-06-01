from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

import uvicorn
import os

from app.api import auth, tasks
from app.api import audit
from app.core.logging import logger

# Inicialização do app
app = FastAPI(title="m00-backend")

# Log de inicialização
logger.info("Iniciando m00-backend")
logger.info("=== Teste de gravação em arquivo de log ===")


# 🚨 Handlers de Exceções
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    logger.error(f"HTTP error {exc.status_code} em {request.url}: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation error em {request.url}: {exc.errors()}")
    return JSONResponse(
        status_code=422,
        content={"error": "Dados inválidos", "details": exc.errors()},
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Erro inesperado em {request.url}: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"error": "Erro interno do servidor"},
    )


# 🚀 Rotas principais
@app.get("/", tags=["Root"])
async def read_root():
    logger.info("Rota raiz acessada")
    return {"message": "API Backend Online 🚀"}


@app.get("/health", tags=["Health Check"])
async def health_check():
    return {"status": "ok"}


# 🚀 Inclusão dos routers
app.include_router(tasks.router)
app.include_router(auth.router)
app.include_router(audit.router)

# 🚀 Execução Local e Render.com
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=False)
