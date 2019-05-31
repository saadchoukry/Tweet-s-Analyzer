import json
from pprint import pprint

import py2neo
from py2neo import Node, Relationship, Graph, NodeMatcher

from neo4jAuth import neo4jAuth
from JsonParser import get_json
from search.models import research as R
from py2neo.database import Schema


class nodesRelationshipsCreator:

    def __init__(self):
        server = neo4jAuth()
        self.graph = server.graphAuth()
        self.transaction = self.graph.begin()
        self.nodeCount = 0
        self.res = None

    def delete_all_nodes(self):
        self.graph.delete_all()

    def commit_changes(self):
        self.transaction.commit()
        return self.graph.begin()

    def node_exists(self, nodeLabel, **properties):
        matcher = NodeMatcher(self.graph)
        return matcher.match(nodeLabel, **properties).first()

    def user_exists(self,screenName):
        matcher = NodeMatcher(self.graph)
        return matcher.match("User",screen_name=screenName).first()


    def user_merge(self, primaryKeyValue, **properties):
        nodeMatch = self.user_exists(primaryKeyValue)
        if nodeMatch is None:
            newNode = Node("User", **properties)
            self.transaction.create(newNode)
            self.nodeCount += 1
            return newNode
        else:
            return nodeMatch

    def node_relationship_merge(self, nodeFrom, nodeLabelTo, relationshipLabel, **properties):
        nodeMatch = self.node_exists(nodeLabelTo, **properties)
        if nodeMatch is None:
            newNodeTo = Node(nodeLabelTo, **properties)
            self.transaction.create(newNodeTo)
            RELATIONSHIP = Relationship(nodeFrom, relationshipLabel, newNodeTo)
            self.transaction.create(RELATIONSHIP)
            self.nodeCount += 1
            return newNodeTo
        else:
            RELATIONSHIP = Relationship(nodeFrom, relationshipLabel, nodeMatch)
            self.transaction.create(RELATIONSHIP)
            return nodeMatch

    def addNodes(self, research_id):
        self.delete_all_nodes()
        self.res = R.getResearchById(research_id)
        for tweet in get_json(self.res):
            if "user" in tweet:
                print('user')
                if "entities" in (tweet["user"]):
                    del tweet["user"]["entities"]
                newUser = self.user_merge(tweet["user"]["screen_name"], **tweet["user"])
                self.node_relationship_merge(newUser, "Language", "TALKS", language=tweet["user"]["lang"])
                if str(tweet["user"]["location"]) != "None":
                    self.node_relationship_merge(newUser, "Location", "IS_FROM", location=tweet["user"]["location"])

                newTweet = self.node_relationship_merge(newUser, "Tweet", "HAS_TWEETED", tweetId=str(tweet["id"]),
                                                        text=tweet["text"])

                self.node_relationship_merge(newTweet, "Source", "VIA", source=tweet["source"])

                if str(tweet["geo"]) != 'None' and str(tweet["place"] != 'None'):
                    del tweet["place"]["bounding_box"]
                    del tweet["place"]["attributes"]
                    self.node_relationship_merge(newTweet, "Location", "IS_POSTED_FROM",
                                                 locationId=tweet["geo"]["coordinates"],
                                                 tweetPlace=tweet["place"]["name"])

                for tag in tweet["entities"]["hashtags"]:
                    self.node_relationship_merge(newTweet, "Hashtag", "HAS_TAG", hashtag=tag["text"])

                for mention in tweet["entities"]["user_mentions"]:
                    self.node_relationship_merge(newUser, "User", "HAS_MENTIONED", **mention)

                if "retweeted_status" in tweet:
                    self.node_relationship_merge(newTweet, "Tweet", "HAS_RETWEETED",
                                                 tweetId=tweet["retweeted_status"]["id_str"],
                                                 text=tweet["retweeted_status"]["text"],
                                                 source=tweet["retweeted_status"]["source"])
            self.transaction = self.commit_changes()
        self.res.numberOfNodes = self.nodeCount
        self.res.save()

    def getCurrentNodeLabels(self):
        schema = Schema(self.graph)
        return schema.node_labels, len(schema.node_labels)

    def getCurrentRelationshipsLabels(self):
        schema = Schema(self.graph)
        return schema.relationship_types, len(schema.relationship_types)

    def getNumberOfOccurencesNodes(self, label):
        return int(self.graph.evaluate("MATCH (n:{}) RETURN count(n);".format(label)))

    def getNumberOfOccurencesRelationships(self, label):
        return int((self.graph.evaluate("MATCH (a)-[r:" + label + "]-(b) RETURN count(r);")) / 2)

    def getVizData(self):
        nodeLabels = self.getCurrentNodeLabels()[0]
        numberOfLabelsCounter = self.getCurrentNodeLabels()[1]
        relationshipsLabels = self.getCurrentRelationshipsLabels()[0]
        numberOfRelLabelsCounter = self.getCurrentRelationshipsLabels()[1]
        nodeLabelsCount = {}
        relationShipCount = {}
        for nodeLabel in nodeLabels:
            nodeLabelsCount[nodeLabel] = self.getNumberOfOccurencesNodes(nodeLabel)
        for relationLabel in relationshipsLabels:
            relationShipCount[relationLabel] = self.getNumberOfOccurencesRelationships(relationLabel)
        return nodeLabelsCount, relationShipCount, numberOfLabelsCounter, numberOfRelLabelsCounter
