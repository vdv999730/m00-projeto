import pytest
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
    with pytest.raises(Exception):
        security.decode_access_token(invalid_token)


@pytest.mark.asyncio
async def test_token_expired():
    # Token com validade de 1 segundo
    data = {"sub": "testuser"}
    token = security.create_access_token(data, expires_delta=-1)
    with pytest.raises(Exception):
        security.decode_access_token(token)
