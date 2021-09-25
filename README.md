# Twitter API with Python
This directory contains an example of Python script to create a web server to get data from Twitter.<br />
- Python Framework: Flask <br />
- Unit test: pytest <br />

<hr />

## Usage
### Get tweets by a hashtag. Get the list of tweets with the given hashtag.
Optional parameters:<br />
- limit: integer, specifies the number of tweets to retrieve, the default is 30. The number must be between 10-100.<br />
Example request:<br />
```
curl GET http://localhost:xxxx/hashtags/Python?limit=40
```

### Get user tweets. Get the list of tweets that the user has on his feed in JSON format.
Optional parameters:<br />
- limit: integer, specifies the number of tweets to retrieve, the default is 30. The number must be between 10-100.<br />
Example request:<br />
```
curl GET http://localhost:xxxx/users/twitter?limit=20
```

<hr />

## Setup
### Requirements
- Python 3.9.7
- pip
- Docker (optional)

### Setup for local running 
1. Set the Twitter authentication token in twitter_api\app\twitter_api.py line 4.
```
TWITTER_TOKEN = "XXXXXXXX"
```
2. [Optional] Set Flask environment, Host IP and Port in run.bat line 4-6. 
```
set FLASK_ENV=development
set HOST_IP=localhost
set HOST_PORT=8080
```
3. Open Command Prompt and run this following line
```
$ run.bat
```

### Setup for local testing
1. Set the Twitter authentication token in twitter_api\app\twitter_api.py line 4.
```
TWITTER_TOKEN = "XXXXXXXX"
```
2. Open Command Prompt and run this following line
```
$ test.bat
```

### Setup for local running (as a container)
1. Set the Twitter authentication token in twitter_api\app\twitter_api.py line 4.
```
TWITTER_TOKEN = "XXXXXXXX"
```
2. Open Command Prompt and run this following line
```
$ docker-compose build
```

<hr />

## Testing information 
This project contains unit tests for 3 areas 
1. Server 
- Test accessing to web server home page
- Test getting response from web server API for Searhing Tweets by hashtag
- Test getting response from web server API for Searhing Tweets by hashtag with default tweet limit (30 tweets) 
- Test getting response from web server API for Searhing Tweets by hashtag without hashtag (False positive)
- Test getting response from web server API for Searhing Tweets by username
- Test getting response from web server API for Searhing Tweets by username with default tweet limit (30 tweets) 
- Test getting response from web server API for Searhing Tweets by username without username (False positive)

2. Twitter API 
- Test getting response from Twitter API for Searhing Tweets by hashtag
- Test getting response from Twitter API for Searhing Tweets by username
- Test getting response from Twitter API for Tweets details
- Test getting response from Twitter API for Twitter user details by username
- Test getting response from Twitter API for Twitter user details by user ID

3. Utilities 
- Test converting datetime to specific format
- Test generating response data in specific format with Twitter hashtag 
- Test generating response data in specific format without Twitter hashtag 
- Test converting object type string contains integer number to object type integer
- Test converting object type string without integer number to object type integer

<hr />

## Example output from server
```
$ GET http://localhost:8080/hashtags/helloworld?limit=10

{
    "data": [
        {
            "account": {
                "fullname": "世之介＠仙台 金曜15-17 RADIO3 & SHOWROOM",
                "href": "/yonosuke27",
                "id": "53160085"
            },
            "date": "11:54 AM - 24 Sep 2021",
            "hashtags": [
                "#DunDunDance",
                "#OHMYGIRL",
                "#サイリウムの証明",
                "#放課後プリンセス",
                "#HelloWorld",
                "#WATWING",
                "#ウェスティンホテル仙台",
                "#みやぎオータムボックス"
            ],
            "likes": 0,
            "replies": 0,
            "retweets": 0,
            "text": "M4 #DunDunDance #OHMYGIRL \n\nM5 #サイリウムの証明 #放課後プリンセス \n\nEnd #HelloWorld #WATWING \n\n今日のゲスト：#ウェスティンホテル仙台\nレストラン シンフォニー シェフ M. Shirakawa\nテイクアウトメニュー「#みやぎオータムボックス」\n詳しくは https://t.co/behboTC5cS https://t.co/R6NgCBuMGs"
        },
        {
            "account": {
                "fullname": "Digitalpraveen",
                "href": "/Praveen05983227",
                "id": "1232918625457078272"
            },
            "date": "11:52 AM - 24 Sep 2021",
            "hashtags": [
                "#ceir",
                "#mobilelost",
                "#mobile",
                "#lost",
                "#knowledge",
                "#innovation",
                "#instagramreels",
                "#instagood",
                "#information",
                "#informationtechnology",
                "#helloworld",
                "#digital",
                "#projects"
            ],
            "likes": 0,
            "replies": 0,
            "retweets": 0,
            "text": "Track your lost phone using IMEI no\n\n#ceir \n#mobilelost\n#mobile\n#lost\n#knowledge \n#innovation \n#instagramreels \n#instagood \n#information \n#informationtechnology \n#helloworld \n#digital \n#projects https://t.co/2Ie32Gdywm"
        },
        {
            "account": {
                "fullname": "Carlos Gonzalez B.",
                "href": "/Coyoton46",
                "id": "276100357"
            },
            "date": "11:51 AM - 24 Sep 2021",
            "hashtags": [
                "#HelloWorld"
            ],
            "likes": 0,
            "replies": 0,
            "retweets": 20,
            "text": "RT @Stellmacher20: #HelloWorld https://t.co/acWqB63A5B"
        },
        ...
    ]
}
```

<hr />

## References
- https://developer.twitter.com/en/docs/twitter-api
- https://flask.palletsprojects.com/en/1.1.x/
- https://docs.pytest.org/en/6.2.x/
