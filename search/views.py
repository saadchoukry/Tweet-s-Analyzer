from django.shortcuts import render, redirect

from static.scripts.Twitter_Offstream import byHashTag
from static.scripts.Twitter_Offstream import byScreenName
from static.scripts.Twitter_Stream import twitter_streamer
from .forms import *
from static.scripts.Twitter_Stream.JsonParser import StringToArray
from .models import *
from results import views as resultsViews
from static.scripts.Twitter_Offstream import ByKeyWord


def home(request):
    return render(request, 'template1/homePage.html',
                  {'rn': stats.getNumberOfResearches(), 'tn': stats.getNumberOfTweets(),
                   'nn': stats.getNumberOfNodes()})


def search(request):
    if request.method == "POST":
        if "streamingDuration" in request.POST:
            post = streamSearch(request)
            return redirect(resultsViews.results, post.researchId)
        elif "screen" in request.POST:
            post = screenNameSearch(request)
            return redirect(resultsViews.results, post.researchId)
        elif "tag" in request.POST:
            post = tagSearch(request)
            return redirect(resultsViews.results, post.researchId)
        elif ("keywords" in request.POST) and ("count" in request.POST):
            post = keySearch(request)
            return redirect(resultsViews.results, post.researchId)
        return render(request, 'template1/researchType.html')

    else:
        return render(request, 'template1/researchType.html', locals())


def streamSearch(request):
    form = streamingForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.researchType = researchType.objects.get(type='Stream')
        post = form.save()
        post.numberOfTweets = twitter_streamer.main(request.POST['streamingDuration'],
                                                    StringToArray(request.POST['keywords']),
                                                    post.researchId)
        post.ratio = float(post.numberOfTweets) / float(post.streamingDuration)
        post.resultsFileName = 'static/collected_data/results_{}.json' \
            .format(post.researchId)
        post.save()
        return post


def screenNameSearch(request):
    form = byScreenNameForm(request.POST)
    print(form)
    if form.is_valid():
        post = form.save(commit=False)
        post.researchType = researchType.objects.get(type='OffStream')
        post = form.save()
        byScreenName.main(request.POST["count"], request.POST["since"], request.POST["screen"], post.researchId)
        post.numberOfTweets = request.POST["count"]
        # post.ratio = float(post.numberOfTweets) / float(post.streamingDuration)
        post.resultsFileName = 'static/collected_data/results_{}.json'.format(post.researchId)
        post.save()
        return post


def tagSearch(request):
    form = byHashtagForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.researchType = researchType.objects.get(type='OffStream')
        post = form.save()
        byHashTag.main(request.POST['count'], request.POST['since'], request.POST['tag'], post.researchId)
        post.numberOfTweets = request.POST["count"]
        # post.ratio = float(post.numberOfTweets) / float(post.streamingDuration)
        post.resultsFileName = 'static/collected_data/results_{}.json'.format(post.researchId)
        post.save()
        return post


def keySearch(request):
    form = byKeywordsForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.researchType = researchType.objects.get(type='OffStream')
        post = form.save()
        ByKeyWord.main(request.POST["count"], request.POST["since"], request.POST["keywords"], post.researchId)
        post.numberOfTweets = request.POST["count"]
        # post.ratio = float(post.numberOfTweets) / float(post.streamingDuration)
        post.resultsFileName = 'static/collected_data/results_{}.json'.format(post.researchId)
        post.save()
        return post


def previous(request):
    previousResearches = research.objects.all()
    return render(request, 'template1/previous.html', locals())


def researchChoice(request):
    return render(request, 'template1/researchType.html', locals())
