"""
# 🔧 BLOCO ORIGINAL – Backup Inline
# Nenhum arquivo anterior detectado para auth.py
"""

# 🔐 BLOCO ATUAL
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from core import security

router = APIRouter()

# Usuário fake para exemplo
fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": security.get_password_hash("admin123"),  # 🔥 Altere depois
    }
}

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Usuário incorreto")
    hashed_password = user_dict["hashed_password"]
    if not security.verify_password(form_data.password, hashed_password):
        raise HTTPException(status_code=400, detail="Senha incorreta")
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user_dict["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/ping")
def ping():
    return {"pong": True}

