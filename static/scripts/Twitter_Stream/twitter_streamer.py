# Système
import time
from sys import argv

# Authentification
from authentification import TwitterAuth

# Json Parsing
from JsonParser import jsonParser, jsonParser2

# Twitter Client
from tweepy import StreamListener
from tweepy.streaming import Stream as tweepyStream


class TwitterListener(StreamListener):
    def __init__(self, time_limit, researchId):
        self.start_time = time.time()
        self.limit = time_limit
        self.file = open('static/collected_data/results_{}.json'.format(researchId), 'w')
        super(TwitterListener, self).__init__()

    # Surcharge de la méthode '_data' : Manipulation des données de sortie (raw_data)
    def on_data(self, raw_data):
        if (time.time() - self.start_time) < self.limit:
            print("writing")
            self.file.write(raw_data)
            return True
        else:
            print("closing")
            self.file.close()
            return False

    def on_error(self, status_code):
        if status_code == 420:
            return False  # Dans le cas de dépassement du quota autorisé par Twitter
        print(status_code)


class TwitterStreamer:
    def __init__(self):
        self.authentification = TwitterAuth.authentification_twitter()

    # Sauvegarde des données (Json)
    def stream_tweets(self, time_limit, filter_list, researchId):
        listener = TwitterListener(time_limit, researchId)
        print("Starting streaming ...")
        stream = tweepyStream(self.authentification, listener)
        stream.filter(track=filter_list)  # Filtres (par mot-clé / liste de mots-clés)
        print("Ending streaming ...")


def main(arg1, arg2, researchId):
    streamer = TwitterStreamer()
    streamer.stream_tweets(float(arg1), arg2, researchId)
    return jsonParser2(researchId)


if __name__ == "__main__":
    main(argv[1], argv[2:])
