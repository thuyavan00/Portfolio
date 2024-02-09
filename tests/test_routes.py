# test_routes.py
from app import create_app

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to My App' in response.data
