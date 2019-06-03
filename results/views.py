from pprint import pprint

from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404
from django.shortcuts import render
import json

from django.utils.safestring import SafeString
from search.models import research as R
from countryToAlpha3 import countryToALpha3
from nodesRelationshipsCreator import nodesRelationshipsCreator


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
    dataToSendToJs = json.dumps(converter.countryCounter, cls=DjangoJSONEncoder)
    return render(request, 'template1/mapping.html', locals())


# MAPPING [END]


graphData = None
# VISUALIZATION
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
def advancedStats(request):
    global graphData
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
        cypherReq = "CALL algo.pageRank.stream('{}', '{}', {{iterations:20, dampingFactor:0.85}}) YIELD nodeId , " \
                    "score RETURN algo.asNode(nodeId).{} AS page , score ORDER BY score DESC LIMIT 5".format(top["nodeLabel"], top["relationShip"], top["attribute"])
        resultsDict.append(graphData.run(cypherReq).data())
    print(resultsDict)
    return render(request, 'template1/advancedStats.html',{'results':resultsDict
        ,'inputs':nodeRelationDict})
# ADVANCED STATS [END]
