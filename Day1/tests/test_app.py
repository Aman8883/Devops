import sys
import os
import pytest
from app.main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code ==200
    assert response.json['status'] == 'healthy'

def test_create_task(client):
    response = client.post('/tasks',json={'title':'Learn Devops'},content_type='application/json')
    assert response.status_code==201
    assert 'id' in response.json
