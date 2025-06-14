# tests/test_auth.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_signup():
    r = client.get("/signup")
    assert r.status_code == 200
    assert "Sign Up" in r.text

def test_post_errors():
    r = client.post("/signup", data={
        "username": "u", "email": "x@x.com",
        "password": "123", "confirm": "456"
    })
    assert "Passwords do not match." in r.text


def test_post_success():
    r = client.post("/signup", data={
        "username": "user1", "email": "a@b.com",
        "password": "password123", "confirm": "password123"
    })
    assert r.status_code == 303
    assert r.headers["location"] == "/welcome"