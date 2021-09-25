import requests
import urllib.parse
 
TWITTER_TOKEN = "" # REQUIRED
DEFAULT_LIMIT = 30
TWITTER_API_BASE = "https://api.twitter.com/2"
DEFAULT_TWEET_FIELDS = "author_id,created_at,entities,public_metrics"

class TwitterAPI:
    def __init__(
        self
    ):  
        self.headers = {"Authorization": "Bearer " + TWITTER_TOKEN}

    def search_by_hashtag(
        self,
        hashtag: str,
        limit: int
    ):  
        """
        To get Tweets by searching from hashtag

        :param hashtag: Twitter hashtag 
        :param limit: Maximum number of tweets fetching. The number must be between 10-100.
        :return: Response from Twitter API with data eg. tweet id, text
        """

        limit = DEFAULT_LIMIT if (limit == None or limit < 10) else limit
        hashtag_parse = urllib.parse.quote_plus(hashtag)
        url = TWITTER_API_BASE + "/tweets/search/recent?query=%23" + hashtag_parse + "&max_results=" + str(limit)
        print("Sending request to Twitter API: " + url)
        response = requests.get(url, headers=self.headers)

        return response

    def search_by_user(
        self,
        username: str,
        limit: int
    ):
        """
        To get Tweets by searching from user who tweeted

        :param username: Twitter username 
        :param limit: Maximum number of tweets fetching. The number must be between 10-100.
        :return: Response from Twitter API with data eg. tweet id, text
        """

        limit = DEFAULT_LIMIT if (limit == None or limit < 10) else limit
        url = TWITTER_API_BASE + "/tweets/search/recent?query=from:" + username + "&max_results=" + str(limit)
        print("Sending request to Twitter API: " + url)
        response = requests.get(url, headers=self.headers)

        return response

    def get_tweets_details(
        self,
        tweet_ids: list
    ):  
        """
        To get Tweets details

        :param tweet_ids: list of Tweet id 
        :return: Response from Twitter API with data eg. created_at, author_id, lang, source, public_metrics, context_annotations, entities
        """

        url = TWITTER_API_BASE + "/tweets?ids=" + (','.join(id for id in tweet_ids)) + "&tweet.fields=" + DEFAULT_TWEET_FIELDS
        print("Sending request to Twitter API: " + url)
        response = requests.get(url, headers=self.headers)

        return response

    def get_user_details_by_username(
        self,
        username: str 
    ):
        """
        To get Twitter user details

        :param username: username of the Twitter user 
        :return: Response from Twitter API with data eg. user id, name, username
        """

        url = TWITTER_API_BASE + "/users/by/username/" + username
        print("Sending request to Twitter API: " + url)
        response = requests.get(url, headers=self.headers)

        return response

    def get_user_details_by_id(
        self,
        userId: str 
    ):
        """
        To get Twitter user details

        :param userId: user ID of the Twitter user 
        :return: Response from Twitter API with data eg. user id, name, username
        """

        url = TWITTER_API_BASE + "/users/" + userId
        print("Sending request to Twitter API: " + url)
        response = requests.get(url, headers=self.headers)

        return response