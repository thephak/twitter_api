import os
import pytest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.server import app

def test_asset():
    assert True

def test_home_page(client):
    response = client.get("/") 
    assert response.status_code == 200
    assert b"Welcome to Twitter API Server!" in response.data

def test_hashtags(client):
    response = client.get("/hashtags/helloworld?limit=10") 
    assert response.status_code == 200
    data = response.json
    assert len(data["data"]) == 10

def test_hashtags_default_limit(client):
    response = client.get("/hashtags/helloworld") 
    assert response.status_code == 200
    data = response.json
    assert len(data["data"]) == 30

def test_hashtags_no_hashtag(client):
    response = client.get("/hashtags/?limit=10") 
    assert response.status_code == 404
    
def test_users(client):
    response = client.get("/users/netflix?limit=10") 
    assert response.status_code == 200
    data = response.json
    assert len(data["data"]) == 10

def test_users_default_limit(client):
    response = client.get("/users/netflix") 
    assert response.status_code == 200
    data = response.json
    assert len(data["data"]) == 30

def test_users_no_username(client):
    response = client.get("/users/?limit=10") 
    assert response.status_code == 404

@pytest.fixture
def client():
    """A test client for the app."""
    return app.test_client()