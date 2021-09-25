import os
import pytest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.twitter_api import TwitterAPI

def test_asset():
    assert True

def test_search_by_hashtag(client):
    response = client.search_by_hashtag(hashtag="helloworld", limit=10)
    data = response.json()
    assert response.status_code == 200
    assert len(data["data"]) == 10
    assert ("helloworld" in data["data"][0]["text"].lower())

def test_search_by_user(client):
    response = client.search_by_user(username="netflix", limit=10)
    data = response.json()
    assert response.status_code == 200
    assert len(data["data"]) == 10

def test_get_tweets_details(client):
    ids = ["1441085134959087621", "1441085130487975952"]
    response = client.get_tweets_details(tweet_ids=ids)
    data = response.json()
    assert response.status_code == 200
    assert len(data["data"]) == 2
    assert (data["data"][0]["id"] in ids)

def test_get_user_details_by_username(client):
    username="netflix"
    response = client.get_user_details_by_username(username=username)
    data = response.json()
    assert response.status_code == 200
    assert (data["data"]["username"].lower() == username)

def test_get_user_details_by_id(client):
    userId="16573941"
    response = client.get_user_details_by_id(userId=userId)
    data = response.json()
    assert response.status_code == 200
    assert (data["data"]["id"] == userId)

@pytest.fixture
def client():
    """A test client for the app."""
    return TwitterAPI()