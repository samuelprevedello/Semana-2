from app.main import app

def test_home():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.get_json().get("message") == "Hello, DevOps (Semana 2)!"

def test_health():
    from app.main import app
    client = app.test_client()
    r = client.get('/health')
    assert r.status_code == 200
    assert r.get_json().get('status') == 'ok'

