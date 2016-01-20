# Necessary imports
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import sys

results = []

class StdOutListener(StreamListener):
    def __init__(self, limit, api=None):
        super(StdOutListener, self).__init__()
        self.num_tweets = limit

    def on_data(self, data):
        if num_tweets < 10:
            results.append(data)
            num_tweets += 1
            return True
        else:
            return False

    def on_error(self, status):
        print status

def authenticate(app):
    auth = OAuthHandler(app['consumer_key'], app['consumer_secret'])
    auth.set_access_token(app['access_token'], app['access_token_secret'])

    return auth

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

def fetchData(app, keywords, limit=10):
    l = StdOutListener()

    auth = authenticate(app)
    stream = Stream(auth, l)

    stream.filter(track=keywords)
    return results
