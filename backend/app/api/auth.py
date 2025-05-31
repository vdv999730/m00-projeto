from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from app.core import security
from app.core.database import get_db
from app.models.user import User as UserModel
from app.schemas.user import UserOut

router = APIRouter(
    prefix="/auth",  # aqui prefix é OK
    tags=["auth"]
)

@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(UserModel).filter(UserModel.username == form_data.username).first()
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"}
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
