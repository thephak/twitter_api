import os
import json

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.utils import *

def test_asset():
    assert True

def test_get_datetime():
    input = "2021-08-13T12:34:56.000Z"
    expected_output = "12:34 PM - 13 Aug 2021"
    output = get_datetime(input)
    assert (output == expected_output)

def test_get_data_with_hashtag():
    # Get data from JSON file
    with open(f'tests/test_data/user.json') as f:
        user_data = json.load(f)
    with open(f'tests/test_data/tweet_with_hashtag.json') as f:
        tweet_data = json.load(f)

    output = get_data(user_data=user_data, tweet_data=tweet_data)
    
    assert output["account"]["fullname"] == user_data["name"]
    assert output["account"]["href"] == "/" + user_data["username"]
    assert output["account"]["id"] == user_data["id"]
    assert ("hashtags" in output)
    assert output["likes"] == tweet_data["public_metrics"]["like_count"]
    assert output["replies"] == tweet_data["public_metrics"]["reply_count"]
    assert output["retweets"] == tweet_data["public_metrics"]["retweet_count"]
    assert output["text"] == tweet_data["text"]

def test_get_data_no_hashtag():
    # Get data from JSON file
    with open(f'tests/test_data/user.json') as f:
        user_data = json.load(f)
    with open(f'tests/test_data/tweet_no_hashtag.json') as f:
        tweet_data = json.load(f)

    output = get_data(user_data=user_data, tweet_data=tweet_data)
    
    assert output["account"]["fullname"] == user_data["name"]
    assert output["account"]["href"] == "/" + user_data["username"]
    assert output["account"]["id"] == user_data["id"]
    assert ("hashtags" not in output)
    assert output["likes"] == tweet_data["public_metrics"]["like_count"]
    assert output["replies"] == tweet_data["public_metrics"]["reply_count"]
    assert output["retweets"] == tweet_data["public_metrics"]["retweet_count"]
    assert output["text"] == tweet_data["text"]

def test_to_int():
    input = "123456"
    expected_output = 123456
    output = to_int(input)
    assert (output == expected_output)

def test_to_int_nonumber():
    input = "abcdef"
    expected_output = 0
    output = to_int(input)
    assert (output == expected_output)
