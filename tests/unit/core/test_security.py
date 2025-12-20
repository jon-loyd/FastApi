import pytest
from app.core.security import hash_password, verify_password

@pytest.mark.parametrize(
    "password",
    [
        "password",
        "P@ssw0rd!",
        "LongAndComplexPasswordIsLong",
        "password with spaces",
        "1234567890",
    ],
)
def test_password_is_hashed(password):
    """
    Happy path round-trip tests
    """
    hashed = hash_password(password)

    assert isinstance(hashed, str)
    assert hashed != password
    assert len(hashed) > 20

    assert verify_password(password, hashed) is True

def test_same_password_generates_different_hashes():
    """
    Ensure hashing security
    """
    password = "password"

    hash1 = hash_password(password)
    hash2 = hash_password(password)

    assert verify_password(password, hash1)
    assert verify_password(password, hash2)
    assert hash1 != hash2
