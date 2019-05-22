from py2neo import Graph

from neo4JCredentials import *


class neo4jAuth:
    def __init__(self):
        self.boltServer = BOLTSERVER
        self.user = USER
        self.password = PASSWORD

    def graphAuth(self):
        graph = Graph(self.boltServer, user=self.user, password=self.password)
        return graph
