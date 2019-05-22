import py2neo
from py2neo import Node, Relationship,Graph,NodeMatcher

from neo4jAuth import neo4jAuth
from JsonParser import get_json
from search.models import research as R

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

    def addNodes(self,research_id):
        self.delete_all_nodes()
        self.res = R.getResearchById(research_id)
        for tweet in get_json(self.res):
            if "entities" in (tweet["user"]):
                del tweet["user"]["entities"]
            newUser = Node("User", **tweet["user"])
            newUser.__primarykey__ = "screen_name"
            newUser.__primarylabel__ = "User"
            self.graph.merge(newUser)
            #self.transaction.create(newUser)
            self.nodeCount += 1
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

