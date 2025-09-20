from app.main import read_root, health_check

def test_root():
    response = read_root()
    assert response == {"message": "Hello from CI/CD pipeline demo!"}

def test_health():
    response = health_check()
    assert response["status"] == "ok"
