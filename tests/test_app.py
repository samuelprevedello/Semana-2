import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app


def test_home_status_and_message():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json().get("message") == "Hello, DevOps!"


def test_home_content_type_json():
    client = app.test_client()
    resp = client.get("/")
    assert resp.headers.get("Content-Type").startswith("application/json")


def test_health_status_and_ok():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json().get("status") == "ok"


def test_health_content_type_json():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.headers.get("Content-Type").startswith("application/json")


def test_post_root_method_not_allowed():
    client = app.test_client()
    resp = client.post("/")
    assert resp.status_code in (405, 500)  # 405 esperado para rota GET


def test_unknown_route_returns_404():
    client = app.test_client()
    resp = client.get("/nao-existe")
    assert resp.status_code == 404
