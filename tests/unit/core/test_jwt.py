from datetime import timedelta
from fastapi import HTTPException
import pytest
from app.core.jwt import create_access_token, verify_access_token

def test_create_and_verify_access_token_roundtrip():
    """
    Happy-path roundtrip test
    """
    sub_data = "1234569789"
    data = {"sub": sub_data}

    token = create_access_token(data)
    decoded_token = verify_access_token(token)

    assert decoded_token == sub_data

def test_expired_token_raises_401():
    """
    Ensure tokens expire
    """
    token = create_access_token(
        {"sub": "1234569789"},
        expires_delta=timedelta(seconds=-1)
    )

    with pytest.raises(HTTPException, match='Token has expired') as e:
        verify_access_token(token)

    assert e.value.status_code == 401

def test_token_missing_sub_raises_401():
    """
    Ensure tokens without subs raise 401
    """
    token = create_access_token({"no": "sub"})

    with pytest.raises(HTTPException, match="Invalid token payload") as e:
        verify_access_token(token)

    assert e.value.status_code == 401

@pytest.mark.parametrize(
    "token",
    [
        "",
        "this isnt a jwt",
        "dashes-are-not-good",
        "nor.periods"
    ]
)
def test_invalid_tokens_raise_401(token):
    """
    Tests to ensure invalid tokens raise 401
    """
    with pytest.raises(HTTPException) as e:
        verify_access_token(token)

    assert e.value.status_code == 401
