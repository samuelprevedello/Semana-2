from app.main import app

def test_home():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.get_json().get("message") == "Hello, DevOps (Semana 2)!"