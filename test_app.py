from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.data == b"Hello, CI/CD with GitHub Actions!"
