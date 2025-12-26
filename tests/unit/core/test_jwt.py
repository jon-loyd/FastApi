from datetime import timedelta
from fastapi import HTTPException
import pytest
from app.core.jwt import create_access_token, verify_access_token

def test_create_and_verify_access_token_roundtrip():
    sub_data = "1234569789"
    data = {"sub": sub_data}

    token = create_access_token(data)
    decoded_token = verify_access_token(token)

    assert decoded_token == sub_data

def test_expired_token_raises_401():
    token = create_access_token(
        {"sub": "1234569789"},
        expires_delta=timedelta(seconds=-1)
    )

    with pytest.raises(HTTPException, match='Token has expired') as e:
        verify_access_token(token)

    assert e.value.status_code == 401
