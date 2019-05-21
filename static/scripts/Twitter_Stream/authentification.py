# Authentification
# Clés

# Twitter Module
from tweepy import *


# Authentification
from static.scripts.Twitter_Stream import credentials


class TwitterAuth:
    @staticmethod
    def authentification_twitter():
        authentification = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
        authentification.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
        return authentification




