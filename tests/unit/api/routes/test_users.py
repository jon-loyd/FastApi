from app.db.deps import get_current_user
from app.main import app


test_user = {"id": 1, "email": "test@test.com"}

def test_me_success(client):
    app.dependency_overrides[get_current_user] = lambda: test_user
    response = client.get("/users/me")
    assert response.status_code == 200
    data = response.json()
    assert data == test_user
    app.dependency_overrides.clear()

def test_me_unauthorized(client):
    response = client.get("/users/me")
    assert response.status_code == 401
    data = response.json()
    assert data["detail"] == "Not authenticated"
