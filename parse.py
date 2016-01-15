# Necessary imports
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import sys
import pandas as pd
import re

def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

if __name__ == '__main__':
    file = open(sys.argv[1], 'r')
    tweetsRaw = []

    for line in file:
        try:
            tweet = json.loads(line)
            tweetsRaw.append(tweet)
        except:
            continue

    outJson = json.dumps({"data": tweetsRaw})
    with open(sys.argv[2], 'w') as outfile:
        json.dump(outJson, outfile)

    tweets = pd.DataFrame()
    tweets['text'] = map(lambda tweet: tweet['text'], tweetsRaw)
    tweets['lang'] = map(lambda tweet: tweet['lang'], tweetsRaw)
    tweets['country'] = map(lambda tweet: tweet['place']['country'] if
        tweet['place'] != None else None, tweetsRaw)

    tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))
    print tweets['link']
