def test_register_success(client_with_db):
    payload = {
        "email": "test@test.com",
        "password": "password123"
    }

    response = client_with_db.post("/auth/register", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["email"] == payload["email"]

def test_register_duplicate_email(client_with_db):
    payload = {
        "email": "test@test.com",
        "password": "password123"
    }

    client_with_db.post("/auth/register", json=payload)
    duplicate_response = client_with_db.post("/auth/register", json=payload)

    assert duplicate_response.status_code == 400
    assert duplicate_response.json()["detail"] == "Email already registered"

def test_login_success(client_with_db):
    payload = {
        "email": "test@test.com",
        "password": "password123"
    }

    client_with_db.post("/auth/register", json=payload)
    response = client_with_db.post("/auth/login", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_password(client_with_db):
    original_password_payload = {
        "email": "test@test.com",
        "password": "password123"
    }
    wrong_password_payload = {
        "email": "test@test.com",
        "password": "wrongpassword"
    }

    client_with_db.post("/auth/register", json=original_password_payload)
    response = client_with_db.post("/auth/login", json=wrong_password_payload)

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"

def test_login_nonexistent_user(client_with_db):
    payload = {
        "email": "nonexistentuser@test.com",
        "password": "password123"
    }

    response = client_with_db.post("/auth/login", json=payload)

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"
