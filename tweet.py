# Necessary imports
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import sys

class StdOutListener(StreamListener):
    def __init__(self, limit):
        self.count = 0
        self.limit = limit
        self.results = []

    def on_data(self, data):
        if self.count < self.limit:
            # print data
            self.results.append(data)
            self.count += 1
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
        self.auth = self.authenticate(app)

    def cleanRaw(self, obj):
        ret={}
        ret["created_at"] = obj["created_at"]
        ret["text"] = obj["text"]
        ret["source"] = obj["source"]
        ret["truncated"] = obj["truncated"]

        ret["user"] = {}
        ret["user"]["location"] = obj["user"]["location"]
        ret["user"]["followers_count"] = obj["user"]["followers_count"]

        if obj["retweeted"]:
            ret["retweeted_status"] = {}
            ret["retweeted_status"]["place"] = {}
            ret["retweeted_status"]["place"]["place_type"] = obj["retweeted_status"]["place"]["place_type"]
            ret["retweeted_status"]["place"]["name"] = obj["retweeted_status"]["place"]["name"]
            ret["retweeted_status"]["place"]["full_name"] = obj["retweeted_status"]["place"]["full_name"]
            ret["retweeted_status"]["place"]["country_code"] = obj["retweeted_status"]["place"]["country_code"]
            ret["retweeted_status"]["place"]["country"] = obj["retweeted_status"]["place"]["country"]

            ret["retweeted_status"]["user"] = {}
            ret["retweeted_status"]["user"]["location"] = obj["retweeted_status"]["user"]["location"]
            ret["retweeted_status"]["user"]["followers_count"] = objret["retweeted_status"]["user"]["followers_count"]

            ret["retweeted_status"]["retweet_count"] = obj["retweeted_status"]["retweet_count"]
            ret["retweeted_status"]["favorite_count"] = obj["retweeted_status"]["favorite_count"]

        ret["entities"] = {}
        ret["entities"]["user_mentions"] = obj["entities"]["user_mentions"]

        return ret

    def fetchData(self, keywords, limit):
        l = StdOutListener(limit)
        stream = Stream(self.auth, l)
        stream.filter(track=keywords)
        return l.results
        # return map(lambda x: self.cleanRaw(json.loads(x)), l.results)
