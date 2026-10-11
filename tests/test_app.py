# Tests for NowPageGen
# Author: Mourad.Soltani

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'
    assert data['author'] == 'Mourad.Soltani'

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'NowPageGen' in response.data

def test_generate(client):
    response = client.post('/generate', data={
        'name': 'Test User',
        'working_on': 'Shipping features',
        'reading': 'Books',
        'exploring': 'Ideas',
        'note': 'Hello'
    })
    assert response.status_code == 200
    assert b"Test User's Now" in response.data
    assert b'Shipping features' in response.data
    assert b'Mourad.Soltani' in response.data
