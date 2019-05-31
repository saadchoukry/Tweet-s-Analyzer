# Système
import json
import time
from sys import argv

# Authentification
from tweepy import API, Cursor

from authentification import TwitterAuth



# Twitter Client

class getTweetsByHashTags:
    def __init__(self, count, since,hashTags,researchId):
        self.authentification = TwitterAuth.authentification_twitter()
        self.hashTags = hashTags
        self.count = count
        self.since = since
        self.tweetsCounter = 0
        self.file = open('static/collected_data/results_{}.json'.format(researchId), 'w')


    def hashTagFormatter(self):
        if self.hashTags[0] != '#':
            self.hashTags = "#" + self.hashTags

    def getTweets(self):
        self.hashTagFormatter()
        tweets = []
        api = API(self.authentification)
        for tweet in Cursor(api.search,q=self.hashTags, since=self.since).items(int(self.count)):
            tweets.append(json.dumps(tweet._json))
            self.tweetsCounter += 1
        new_data = "[" + ",".join(tweets) + "]"
        self.file.write(new_data)


def main(count, since,hashtags , researchId):
    getTweets = getTweetsByHashTags(count, since,hashtags,researchId)
    getTweets.getTweets()
    return getTweets.tweetsCounter


