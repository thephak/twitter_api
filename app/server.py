import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request
from app.twitter_api import TwitterAPI
from app.utils import get_data, to_int

app = Flask(__name__)
HOST_IP = os.getenv("HOST_IP")
HOST_PORT = os.getenv("HOST_PORT")

@app.route('/')
def index():
    return "Welcome to Twitter API Server!"


@app.route('/hashtags/<string:hashtag>', methods=['GET'])
def hashtags(hashtag):
    """
    Adding URL path for API to search for Tweets by hashtag
    """

    print ("Searching Tweets from Hashtag: " + hashtag)

    if hashtag == None or hashtag == "":
        return "Hashtag cannot be blank.", 400, {'Content-Type': 'text/plain; charset=utf-8'}

    limit_int = 0
    if "limit" in request.args:
        limit_int = to_int(request.args.get("limit"))
        if limit_int < 10 or limit_int > 100:
            return "Search limit is not between 10 and 100.", 400, {'Content-Type': 'text/plain; charset=utf-8'}

    tweets = []

    try:
        twitter_api = TwitterAPI()
        # Get Tweets by hashtag from Twitter API
        response = twitter_api.search_by_hashtag(hashtag, limit_int)
        
        if response.status_code != 200:
            error_msg = "An error occurred during the call to Twitter API"
            return error_msg, response.status_code, {'Content-Type': 'text/plain; charset=utf-8'}
        
        data = response.json() 
        tweet_ids = [tweet["id"] for tweet in data["data"]]
        
        # Get Tweet details by Tweet ID from Twitter API
        response = twitter_api.get_tweets_details(tweet_ids)
        if response.status_code != 200:
            error_msg = "An error occurred during the call to Twitter API"
            return error_msg, response.status_code, {'Content-Type': 'text/plain; charset=utf-8'}

        data = response.json()
        for tweet_data in data["data"]:
            # Get Twitter User details by User ID from Twitter API
            response = twitter_api.get_user_details_by_id(tweet_data["author_id"])
            
            if response.status_code != 200:
                error_msg = "An error occurred during the call to Twitter API"
                return error_msg, response.status_code, {'Content-Type': 'text/plain; charset=utf-8'}

            user = response.json()

            # Generate output data to send back as a response
            tweet = get_data(user["data"], tweet_data)
            tweets.append(tweet)

        return {"data": tweets}, 200, {'Content-Type': 'application/json; charset=utf-8'}
            
    except Exception as e:
        return e, 400, {'Content-Type': 'text/plain; charset=utf-8'}


@app.route('/users/<string:username>', methods=['GET'])
def users(username):
    """
    Adding URL path for API to search for Tweets by hashtag
    """

    print ("Searching Tweets from User: " + username)

    if username == None or username == "":
        return "Username cannot be blank.", 400, {'Content-Type': 'text/plain; charset=utf-8'}

    limit_int = 0
    if "limit" in request.args:
        limit_int = to_int(request.args.get("limit"))
        if limit_int < 10 or limit_int > 100:
            return "Search limit is not between 10 and 100.", 400, {'Content-Type': 'text/plain; charset=utf-8'}

    tweets = []

    try:
        twitter_api = TwitterAPI()
        # Get Tweets by user from Twitter API
        response = twitter_api.get_user_details_by_username(username)
        
        if response.status_code != 200:
            error_msg = "An error occurred during the call to Twitter API"
            return error_msg, response.status_code, {'Content-Type': 'text/plain; charset=utf-8'}

        # Get Twitter User details by Username from Twitter API
        user = response.json()
        response = twitter_api.search_by_user(username, limit_int)
        if response.status_code != 200:
            error_msg = "An error occurred during the call to Twitter API"
            return error_msg, response.status_code, {'Content-Type': 'text/plain; charset=utf-8'}
        
        data = response.json()  
        tweet_ids = [tweet["id"] for tweet in data["data"]]

        # Get Tweet details by Tweet ID from Twitter API
        response = twitter_api.get_tweets_details(tweet_ids)
        if response.status_code != 200:
            error_msg = "An error occurred during the call to Twitter API"
            return error_msg, response.status_code, {'Content-Type': 'text/plain; charset=utf-8'}

        data = response.json()
        for tweet_data in data["data"]:
            # Generate output data to send back as a response
            tweet = get_data(user["data"], tweet_data)
            tweets.append(tweet)

        return {"data": tweets}, 200, {'Content-Type': 'application/json; charset=utf-8'}
            
    except Exception as e:
        return e, 400, {'Content-Type': 'text/plain; charset=utf-8'}


if __name__ == "__main__":
    app.run(host=HOST_IP, port=to_int(HOST_PORT), debug=True)
