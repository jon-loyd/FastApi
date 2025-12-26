from app.core.jwt import create_access_token, verify_access_token

def test_create_and_verify_access_token_roundtrip():
    sub_data = "1234569789"
    data = {"sub": sub_data}

    token = create_access_token(data)
    decoded_token = verify_access_token(token)

    assert decoded_token == sub_data
