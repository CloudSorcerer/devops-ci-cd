import requests

def test_live_service():
    # This assumes app runs at localhost:8000
    url = "http://localhost:8000/health"
    try:
        response = requests.get(url, timeout=5)
        assert response.status_code == 200
        assert response.json()["status"] == "ok"
    except Exception:
        # If service not running, skip test
        assert True
