# Necessary imports
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import sys

class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        return True

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

def fetchData(app, keywords):
    l = StdOutListener()

    auth = authenticate(app)
    stream = Stream(auth, l)

    stream.filter(track=keywords)

if __name__ == '__main__':

    # Extracting keywords from args
    keywords = sys.argv[2:]
    with open(sys.argv[1]) as data_file:
        app = json.load(data_file)

    # Fetching data from keywords
    fetchData(app, keywords)
