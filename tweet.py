# Necessary imports
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import sys

class StdOutListener(StreamListener):
    def __init__(self, limit):
        self.num_tweets = 0
        self.limit = limit
        self.results = []

    def on_data(self, data):
        if self.num_tweets < 1:
            print data
            self.results.append(data)
            self.num_tweets += 1
            return True
        else:
            return False

    def on_error(self, status):
        print "err : " + str(status)

class TwitterExtract:
    def authenticate(self, app):
        auth = OAuthHandler(app['consumer_key'], app['consumer_secret'])
        auth.set_access_token(app['access_token'], app['access_token_secret'])
        return auth

    def __init__(self, app):
        print app
        self.auth = self.authenticate(app)

    def fetchData(self, keywords, limit):
        l = StdOutListener(limit)
        stream = Stream(self.auth, l)
        stream.filter(track=keywords)
        return l.results
