import pytest
from datetime import timedelta
from app.core import security


@pytest.mark.asyncio
async def test_create_access_token_and_decode():
    data = {"sub": "testuser"}
    token = security.create_access_token(data)
    decoded_data = security.decode_access_token(token)
    assert decoded_data["sub"] == "testuser"


@pytest.mark.asyncio
async def test_decode_invalid_token():
    invalid_token = "this.is.an.invalid.token"
    decoded = security.decode_access_token(invalid_token)
    assert decoded is None  # << Corrigido para validar retorno None


@pytest.mark.asyncio
async def test_token_expired():
    data = {"sub": "testuser"}
    # Corrigir aqui: passar um timedelta negativo
    token = security.create_access_token(data, expires_delta=timedelta(seconds=-1))
    decoded = security.decode_access_token(token)
    assert decoded is None  # << Corrigido para validar token expirado
