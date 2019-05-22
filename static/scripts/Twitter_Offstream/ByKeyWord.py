# Système
import json
import time
from sys import argv

# Authentification
from tweepy import API, Cursor

from authentification import TwitterAuth



# Twitter Client

class getTweetsByKeyWords:
    def __init__(self, count, since, keyWords, researchId):
        self.authentification = TwitterAuth.authentification_twitter()
        self.keyWords = keyWords
        self.count = count
        self.since = since
        self.file = open('static/collected_data/results_{}.json'.format(researchId), 'w')

    def keywordFormatter(self):
        while self.keyWords == '#':
            self.keyWords = self.keyWords[1:]

    def getTweets(self):
        self.keywordFormatter()
        tweets = []
        api = API(self.authentification)
        for tweet in Cursor(api.search,
                            q=self.keyWords, since=self.since).items(int(self.count)):
            tweets.append(json.dumps(tweet._json))


        new_data = "[" + ",".join(tweets) + "]"
        self.file.write(new_data)


def main(count, since, keywords, researchId):
    getTweets = getTweetsByKeyWords(count, since, keywords, researchId)
    getTweets.getTweets()
