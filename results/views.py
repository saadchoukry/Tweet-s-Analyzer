from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404
from django.shortcuts import render
import json
from py2neo import Node, Relationship, Graph, NodeMatcher
from search.models import research as R
from geopy.geocoders import Nominatim
import pycountry
from nodesRelationshipsCreator import nodesRelationshipsCreator
from JsonParser import get_json

"""
nodeCount = 0


def graphAuth():
    graph = Graph("bolt://localhost:11001", user="neo4j", password="123456")
    # graph = Graph("bolt://54.174.242.219:32934", user="neo4j", password="liberties-reel-preserver")
    return graph


def commit_changes(graph, transaction):
    transaction.commit()
    newTransaction = graph.begin()
    return newTransaction


def delete_all_nodes(graph):
    transaction = graph.begin()
    graph.delete_all()
    return transaction


def start_visual():
    graph = graphAuth()
    transaction = delete_all_nodes(graph)
    return graph, transaction


def node_exists(graph, nodeLabel, **properties):
    matcher = NodeMatcher(graph)
    return matcher.match(nodeLabel, **properties).first()


def node_relationship_merge(graph, transaction, nodeFrom, nodeLabelTo, relationshipLabel, **properties):
    nodeMatch = node_exists(graph, nodeLabelTo, **properties)
    global nodeCount
    if nodeMatch is None:
        newNodeTo = Node(nodeLabelTo, **properties)
        transaction.create(newNodeTo)
        RELATIONSHIP = Relationship(nodeFrom, relationshipLabel, newNodeTo)
        transaction.create(RELATIONSHIP)
        nodeCount += 1
        return newNodeTo
    else:
        RELATIONSHIP = Relationship(nodeFrom, relationshipLabel, nodeMatch)
        transaction.create(RELATIONSHIP)
        return nodeMatch


def get_json(research):
    jsonFile = open(research.resultsFileName, 'r')
    data = jsonFile.read()
    return json.loads(data)


def addNodes(research):
    global nodeCount

    start = start_visual()
    graph = start[0]
    transaction = start[1]

    for tweet in get_json(research):
        if "entities" in (tweet["user"]):
            del tweet["user"]["entities"]
        newUser = Node("User", **tweet["user"])
        newUser.__primarykey__ = "screen_name"
        newUser.__primarylabel__ = "User"
        # graph.merge(newUser)
        transaction.create(newUser)
        nodeCount += 1
        node_relationship_merge(graph, transaction,
                                newUser, "Language", "TALKS", language=tweet["user"]["lang"])
        if str(tweet["user"]["location"]) != "None":
            node_relationship_merge(graph, transaction,
                                    newUser, "Location", "IS_FROM", location=tweet["user"]["location"])

        newTweet = node_relationship_merge(graph, transaction,
                                           newUser, "Tweet", "HAS_TWEETED", tweetId=str(tweet["id"]),
                                           text=tweet["text"])

        node_relationship_merge(graph,transaction,newTweet,"Source","VIA",source=tweet["source"])

        if str(tweet["geo"]) != 'None' and str(tweet["place"] != 'None'):
            del tweet["place"]["bounding_box"]
            del tweet["place"]["attributes"]
            node_relationship_merge(graph, transaction,
                                    newTweet, "Location", "IS_POSTED_FROM",
                                    locationId=tweet["geo"]["coordinates"],
                                    tweetPlace=tweet["place"]["name"])

        for tag in tweet["entities"]["hashtags"]:
            node_relationship_merge(graph, transaction,
                                    newTweet, "Hashtag", "HAS_TAG", hashtag=tag["text"])

        for mention in tweet["entities"]["user_mentions"]:
            node_relationship_merge(graph, transaction,
                                    newUser, "User", "HAS_MENTIONED", **mention)

        if "retweeted_status" in tweet:
            node_relationship_merge(graph, transaction,
                                    newTweet, "Tweet", "HAS_RETWEETED",
                                    tweetId=tweet["retweeted_status"]["id_str"],
                                    text=tweet["retweeted_status"]["text"],
                                    source=tweet["retweeted_status"]["source"])
        transaction = commit_changes(graph, transaction)
    research.numberOfNodes = nodeCount
    research.save()
    nodeCount = 0
"""



def results(request, research_id):
    if not research_id:
        raise Http404

    research = R.getResearchById(research_id)
    return render(request, 'template1/results.html', locals())


# MAPPING


def getAlpha2Countries(locations):
    countries = []
    geolocator = Nominatim(timeout=60)
    for location in locations:
        geo = geolocator.geocode(location)
        if geo is not None:
            loc = geolocator.reverse("{}, {}".format(geo.latitude, geo.longitude))
            countries.append(loc.raw['address']['country_code'].upper())
    return countries



def getAlpha3Country(alpha2Countries):
    alpha3Countries = []
    # cleanedCountries = countryNameCleaner(alpha2Countries)
    for alpha2country in alpha2Countries:
        c = pycountry.countries.get(alpha_2=alpha2country)
        if c is not None:
            alpha3Countries.append(c.alpha_3)
    return alpha3Countries


def getCountryCount(alpha3Countries):
    countryCount = {}
    total = 0
    for alpha3Country in alpha3Countries:
        total += 1
        if alpha3Country in countryCount:
            countryCount[alpha3Country]["numberOfThings"] += 1
        else:
            countryCount[alpha3Country] = {"fillKey": None, "numberOfThings": 1}
    return countryCount, total


def updateFillKeys(countries_data, totalCount):
    for country in countries_data.values():
        print(country["numberOfThings"] / totalCount)
        if country["numberOfThings"] / totalCount >= 0.6:
            country["fillKey"] = "HIGH"
        if (country["numberOfThings"] / totalCount < 0.6) \
                and (country["numberOfThings"] / totalCount > 0.10):
            country["fillKey"] = "MEDIUM"
        if country["numberOfThings"] / totalCount < 0.10:
            country["fillKey"] = "LOW"
    return countries_data


def getLocations(research):
    locations = []
    for tweet in get_json(research):
        if str(tweet["user"]["location"]) != "None":
            locations.append(tweet["user"]["location"])
    return locations


def mapping(request, research_id):
    if not research_id:
        raise Http404
    research = R.getResearchById(research_id)

    locations = getLocations(research)
    alpha2Countries = getAlpha2Countries(locations)
    alpha3Countries = getAlpha3Country(alpha2Countries)

    getCount = getCountryCount(alpha3Countries)
    dictCountryCount = getCount[0]
    totalCount = getCount[1]

    dataToSendToJs = json.dumps(updateFillKeys(dictCountryCount, totalCount),
                                cls=DjangoJSONEncoder)
    print(dataToSendToJs)

    return render(request, 'template1/mapping.html', locals())


def visualization(request, research_id):
    if not research_id:
        raise Http404
    creator = nodesRelationshipsCreator()
    creator.addNodes(research_id)
    return render(request, 'template1/visualization.html', locals())
