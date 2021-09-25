import json

from app.utils import *


# Get data from JSON file
with open(f'tests/test_data/user.json') as f:
    user_data = json.load(f)
with open(f'tests/test_data/tweet_no_hashtag.json') as f:
    tweet_data = json.load(f)

output = get_data(user_data=user_data, tweet_data=tweet_data)
print(output)