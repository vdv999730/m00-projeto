import pytest
from app.api.dependencies import get_current_user
from app.core import security


@pytest.mark.asyncio
async def test_get_current_user_valid_token():
    data = {"sub": "testuser"}
    token = security.create_access_token(data)
    username = get_current_user(token=token)
    assert username == "testuser"


@pytest.mark.asyncio
async def test_get_current_user_invalid_token():
    invalid_token = "invalid.token.here"
    with pytest.raises(Exception):
        get_current_user(token=invalid_token)
