import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app


def test_home():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.get_json().get("message") == "Hello, DevOps!"


def test_health():
    client = app.test_client()
    resp = client.get('/health')
    assert resp.status_code == 200
    assert resp.get_json().get("status") == "ok"
