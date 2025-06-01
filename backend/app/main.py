from fastapi import FastAPI
from app.api import auth, tasks
from app.core.logging import logger
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI(title="m00-backend")
logger.info("Iniciando m00-backend")
logger.info("=== Teste de gravação em arquivo de log ===")


# Captura exceções HTTP
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    logger.error(f"HTTP error {exc.status_code} em {request.url}: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )


# Captura validações de requisição (Pydantic)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation error em {request.url}: {exc.errors()}")
    return JSONResponse(
        status_code=422,
        content={"error": "Dados inválidos", "details": exc.errors()},
    )


# Captura quaisquer outras exceções não tratadas
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Erro inesperado em {request.url}: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"error": "Erro interno do servidor"},
    )


@app.get("/", tags=["root"])
async def read_root():
    logger.info("Rota raiz acessada")
    return {"message": "API Backend Online 🚀"}


@app.get("/", tags=["Health Check"])
def root():
    return {"message": "Backend is up and running!"}


# 🚨 Inclusão correta dos routers
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(
    auth.router
)  # O router do auth já tem prefix "/auth" dentro do próprio arquivo
