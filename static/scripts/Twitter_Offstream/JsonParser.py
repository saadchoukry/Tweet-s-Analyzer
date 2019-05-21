import datetime
import json
import os
import re


def jsonParser2(researchId):

    file = open('static/scripts/Twitter_stream/collected_data/results_{}.json'.format(researchId),'r')
    data = file.read()
    new_data = "[" + data.replace('\n\n', ',')[:-1] + "]"
    file.close()
    file = open('static/scripts/Twitter_stream/collected_data/results_{}.json'.format(researchId), 'w')
    file.write(new_data)
    file.close()
    json_data = json.loads(new_data)
    print('Data parsed successfully.')
    return len(json_data)



def directoryCreator(keywordsArray, creation_date=datetime.date.today(), search_type="Streaming"):
    directoryName = search_type + "_" + str(creation_date)
    for keyword in keywordsArray:
        directoryName += "_{0}".format(keyword)
    os.mkdir("static/scripts/Twitter_stream/tweets/" + directoryName)
    return directoryName


def jsonParser(keywords):
    file = open('static/scripts/Twitter_stream/streaming_results.json', 'r+')
    data = file.read()
    new_data = "[" + data.replace('\n\n', ',')[:-1] + "]"
    file.close()
    file = open('static/scripts/Twitter_stream/streaming_results.json', 'w')
    file.write(new_data)
    file.close()
    directoryName = directoryCreator(keywords)
    os.chdir("static/scripts/Twitter_stream/tweets/" + directoryName)
    data_json = json.loads(new_data)

    tweets_counter=0
    for singleTweet in data_json:
        fileName = "Tweet_{0}.json".format(str(data_json.index(singleTweet) + 1))
        singlefile = open(fileName, 'w+')
        json.dump(singleTweet, singlefile)
        tweets_counter = data_json.index(singleTweet)
    print("{0} Tweets added .".format(str(tweets_counter - 1)))
    return  tweets_counter


def StringToArray(string):
    array=re.compile(" +").split(string)
    return array