from datetime import datetime 


def get_datetime(
    input: str
):
    """
    Get Datetime in the exact output format.
    :param input: String of datetime in format "2021-09-03T16:54:50.000Z"
    :return: String of datetime in format "2:54 PM - 8 Mar 2018"
    """

    datetime_date = datetime.strptime(input, "%Y-%m-%dT%H:%M:%S.%fZ")
    return datetime_date.strftime("%#I:%M %p - %#d %b %Y")

def get_data(
    user_data: any,
    tweet_data: any 
):
    """
    Get data in exact format. 
    :param user_data: Data from user part
    :param tweet_data: Data from Tweet part
    :return: Data object in format of the AnyMind problem
    """

    if "entities" in tweet_data and "hashtags" in tweet_data["entities"]:
        hashtags = [("#" + hashtag["tag"]) for hashtag in tweet_data["entities"]["hashtags"]]
        data = {
            "account": {
                "fullname": user_data["name"],
                "href": "/" + user_data["username"],
                "id": user_data["id"]
            },
            "date": get_datetime(tweet_data["created_at"]),
            "hashtags": hashtags, 
            "likes": tweet_data["public_metrics"]["like_count"],
            "replies": tweet_data["public_metrics"]["reply_count"],
            "retweets": tweet_data["public_metrics"]["retweet_count"],
            "text": tweet_data["text"]
        }
    else:
        data = {
            "account": {
                "fullname": user_data["name"],
                "href": "/" + user_data["username"],
                "id": user_data["id"]
            },
            "date": get_datetime(tweet_data["created_at"]),
            "likes": tweet_data["public_metrics"]["like_count"],
            "replies": tweet_data["public_metrics"]["reply_count"],
            "retweets": tweet_data["public_metrics"]["retweet_count"],
            "text": tweet_data["text"]
        }        

    return data 

def to_int(
    input: str
):
    """
    Convert string to integer with error handling
    :param input: String that contains integer number
    :return: Interger number or 0 if the the string is not contains integer number 
    """
    
    try: 
        return int(input)
    except ValueError:
        return 0
