from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession  # [NOVO] Para async DB
from sqlalchemy.future import select  # [NOVO] Select assíncrono para buscar usuário
from datetime import timedelta

from app.core import security
from app.core.database import get_db
from app.models.user import User as UserModel
from app.schemas.user import UserOut

# [NOVO] Importação do serviço de auditoria
from app.services.audit_service import log_event

router = APIRouter(prefix="/auth", tags=["auth"])  # aqui prefix é OK


@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),  # [ALTERADO] Para ser async
):
    result = await db.execute(
        select(UserModel).where(UserModel.username == form_data.username)
    )
    user = result.scalars().first()

    if not user or not security.verify_password(
        form_data.password, user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # [NOVO] Audit Log - Login Bem-Sucedido
    await log_event(
        db,
        user_id=user.id,
        action="LOGIN_SUCCESS",
        details="User logged in successfully",
    )

    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me", response_model=UserOut)
async def read_users_me(current_user: UserModel = Depends(security.get_current_user)):
    return current_user


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/version")
def version():
    return {"version": "1.0.0", "system": "m00-backend"}


@router.get("/ping")
def ping():
    return {"pong": True}
