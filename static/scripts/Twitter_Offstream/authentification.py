# Authentification
# Clés

# Twitter Module
from tweepy import *


# Authentification
from credentials import *


class TwitterAuth:
    @staticmethod
    def authentification_twitter():
        authentification = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        authentification.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return authentification




