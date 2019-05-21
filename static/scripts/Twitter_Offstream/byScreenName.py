# Système
import json
from sys import argv

# Authentification
import tweepy
from tweepy import API, Cursor

from .authentification import TwitterAuth


# Json Parsing

# Twitter Client

class getTweetsByScreenName:
    def __init__(self, count, since, screenName, researchId):
        self.authentification = TwitterAuth.authentification_twitter()
        self.screenName = screenName
        self.count = count
        self.since = since
        self.file = open('static/collected_data/results_{}.json'.format(researchId), 'w')

    def getTweets(self):
        tweets = []
        try:
            api = API(self.authentification)
            for tweet in Cursor(api.user_timeline,
                                screen_name=self.screenName, since=self.since).items(int(self.count)):
                tweets.append(json.dumps(tweet._json))

            new_data = "[" + ",".join(tweets) + "]"
            self.file.write(new_data)
        except tweepy.error.TweepError as e1:
            if str(e1.response) == "<Response [404]>":
                return "No user with the given screen name . "


def main(count, since, screenName, researchId):
    getTweets = getTweetsByScreenName(count, since, screenName, researchId)
    getTweets.getTweets()


