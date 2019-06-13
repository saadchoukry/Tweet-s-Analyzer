import collections
import itertools
import operator
from pprint import pprint
from neo4jAuth import neo4jAuth

import py2neo
from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404
from django.shortcuts import render, redirect
import json
from search.models import research as R
from countryToAlpha3 import countryToALpha3
from nodesRelationshipsCreator import nodesRelationshipsCreator


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


# RESULTS
def results(request, research_id):
    if not research_id:
        raise Http404
    research = R.getResearchById(research_id)
    if research.researchType.type == 'Stream':
        keywords = research.getKeywords
        streamingDuration = research.getStreamingDuration
    elif research.researchType.type == 'OffStream':
        since = research.getSince
        count = research.getCount
    else:
        pass
    auth = neo4jAuth()
    graph = auth.graphAuth()
    try:
        neo4jVersion = str(graph.database.kernel_version)
    except Exception:
        print('No connection to database.')
    return render(request, 'template1/results.html', locals())


# RESULTS [END]


# MAPPING
def mapping(request, research_id):
        converter = countryToALpha3(research_id)
        converter.getAlpha2Countries()
        converter.getAlpha3Countries()
        converter.getCountryCount()
        converter.updateFillKeys()
        converter.updateValidLocationsRatio()
        converter.updateInvalidLocationsRatio()
        converter.updateUnknownLocationsRatio()
        mappingStats = json.dumps({'Valid location ratio': converter.validLocationsRatio,
                                   'Invalid location ratio': converter.invalidLocationsRatio,
                                   'Unknown locations ratio': converter.unknownLocationsRatio}
                                  , cls=DjangoJSONEncoder)
        dataToSendToJs = json.dumps(converter.countryCounter, cls=DjangoJSONEncoder)


        for country in converter.countryCounter:
            converter.topCountries[converter.getFullCountry(country)] = converter.countryCounter[country][
                "numberOfThings"]
        sortedCountries = sorted(converter.topCountries.items(), key=operator.itemgetter(1))
        sortedCountriesDict = collections.OrderedDict(sortedCountries)
        sortedCountriesDict = collections.OrderedDict(reversed(list(sortedCountriesDict.items())))
        topCountriesData = collections.OrderedDict(itertools.islice(sortedCountriesDict.items(), 5))
        print(topCountriesData)
        topCountriesData = json.dumps(topCountriesData, cls=DjangoJSONEncoder)
        return render(request, 'template1/mapping.html', locals())


# MAPPING [END]


# VISUALIZATION
graphData = None


def visualization(request, research_id):
    global graphData
    if not research_id:
        raise Http404
    research_id = research_id
    creator = nodesRelationshipsCreator()
    creator.addNodes(research_id)
    data = creator.getVizData()
    nodeLabelsAndCounter = data[0]
    relationshipLabelsAndCounter = data[1]
    nodeLabelCount = data[2]
    relationshipLabelCount = data[3]
    graphData = creator.graph
    return render(request, 'template1/visualization.html', locals())


# VISUALISATION [END]


# ADVANCED STATS
def advancedStats(request, research_id):
    global graphData
    if 'HTTP_REFERER' in request.META:
        if request.META['HTTP_REFERER'] == \
                "http://localhost:8000/results/visualization/{}/".format(research_id)\
                or request.META['HTTP_REFERER'] == "http://127.0.0.1:8000/results/visualization/{}/".format(research_id):
            resultsDict = []
            nodeRelationDict = [
                {
                    'nodeLabel': 'User',
                    'relationShip': 'HAS_MENTIONED',
                    'attribute': 'screen_name'
                },
                {
                    'nodeLabel': 'Tweet',
                    'relationShip': 'HAS_TAG',
                    'attribute': 'text'
                },
                {
                    'nodeLabel': 'User',
                    'relationShip': 'HAS_TWEETED',
                    'attribute': 'screen_name'
                },
                {
                    'nodeLabel': 'Tweet',
                    'relationShip': 'HAS_RETWEETED',
                    'attribute': 'text'
                },
            ]
            for top in nodeRelationDict:
                cypherReq = "CALL algo.pageRank.stream('{}', '{}', {{direction:'BOTH', iterations:20, dampingFactor:0.85}}) YIELD nodeId , " \
                            "score RETURN algo.asNode(nodeId).{} AS page , score ORDER BY score DESC LIMIT 5".format(
                    top["nodeLabel"], top["relationShip"], top["attribute"])
                resultsDict.append(graphData.run(cypherReq).data())
            dataToSendToJs = json.dumps(resultsDict, cls=DjangoJSONEncoder)
            return render(request, 'template1/advancedStats.html', {'results': resultsDict
                , 'inputs': nodeRelationDict,'dataToSendToJs':dataToSendToJs})
        else:
            return render(request,'500.html')
    else:
        return render(request,'500.html')
# ADVANCED STATS [END]
