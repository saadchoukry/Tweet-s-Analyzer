import time

from django.shortcuts import render, redirect
from .forms import *
from .models import *

import byHashTag
import byScreenName
import twitter_streamer
from JsonParser import StringToArray
from results import views as resultsViews
import ByKeyWord
from JsonParser import uploadedTweetsParser


def handler404(request,exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request,'500.html', status=500)


def home(request):
    return render(request, 'template1/homePage.html',
                  {'rn': stats.getNumberOfResearches(), 'tn': stats.getNumberOfTweets(),
                   'nn': stats.getNumberOfNodes()})


def search(request):
    if request.method == "POST":
        if "streamingDuration" in request.POST:
            post = streamSearch(request)
            if str(type(post)) == "<class 'django.http.response.HttpResponse'>":
                return post
            else:
                return redirect(resultsViews.results, post.researchId)

        elif "screen" in request.POST:
            post = screenNameSearch(request)
            if str(type(post)) == "<class 'django.http.response.HttpResponse'>":
                return post
            else:
                return redirect(resultsViews.results, post.researchId)
        elif "tag" in request.POST:
            post = tagSearch(request)
            if str(type(post)) == "<class 'django.http.response.HttpResponse'>":
                return post
            else:
                return redirect(resultsViews.results, post.researchId)
        elif ("keywords1" in request.POST) and ("count" in request.POST):
            post = keySearch(request)
            if str(type(post)) == "<class 'django.http.response.HttpResponse'>":
                return post
            else:
                return redirect(resultsViews.results, post.researchId)
    else:
        return render(request, 'template1/researchType.html', locals())


def uploadTweets(request):
    if request.method == "POST":
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.researchType = researchType.objects.get(type='Upload')
            upload = form.save()
            upload.resultsFileName = 'static/collected_data/results_{}.json' \
                .format(upload.researchId)
            upload.numberOfTweets = uploadedTweetsParser(upload.jsonFile, upload.researchId)
            upload.save()
            return redirect(resultsViews.results, upload.researchId)
        else:
            return render(request, 'template1/uploadTweets.html', locals())
    else:
        return render(request, 'template1/uploadTweets.html', {})


def streamSearch(request):
    form = streamingForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.researchType = researchType.objects.get(type='Stream')
        post = form.save()

        start_time = time.time()
        post.numberOfTweets = twitter_streamer.main(request.POST['streamingDuration'],
                                                    StringToArray(request.POST['keywords']),
                                                    post.researchId)
        post.executionduration = time.time() - start_time
        post.ratio = float(post.numberOfTweets) / float(post.streamingDuration)
        post.resultsFileName = 'static/collected_data/results_{}.json' \
            .format(post.researchId)
        post.save()
        return post
    else:
        return render(request, 'template1/researchType.html', {'form0': form})


def screenNameSearch(request):
    form = byScreenNameForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.researchType = researchType.objects.get(type='OffStream')
        post = form.save()
        start_time = time.time()
        post.numberOfTweets = byScreenName.main(request.POST["count"], request.POST["since"], request.POST["screen"],
                                                post.researchId)
        post.executionDuration = time.time() - start_time
        post.ratio = float(post.numberOfTweets / post.executionDuration)
        post.resultsFileName = 'static/collected_data/results_{}.json'.format(post.researchId)
        post.save()
        return post
    else:
        return render(request, 'template1/researchType.html', {'form': form})


def tagSearch(request):
    form = byHashtagForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.researchType = researchType.objects.get(type='OffStream')
        post = form.save()

        start_time = time.time()
        post.numberOfTweets = byHashTag.main(request.POST['count'], request.POST['since'], request.POST['tag'],
                                             post.researchId)
        post.executionduration = time.time() - start_time
        if post.executionDuration == 0.0:
            post.ratio = 0
        else:
            post.ratio = float(post.numberOfTweets / post.executionDuration)

        post.resultsFileName = 'static/collected_data/results_{}.json'.format(post.researchId)
        post.save()
        return post
    else:
        return render(request, 'template1/researchType.html', {'form': form})


def keySearch(request):
    form = byKeywordsForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.researchType = researchType.objects.get(type='OffStream')
        post = form.save()

        start_time = time.time()
        post.numberOfTweets = ByKeyWord.main(request.POST["count"], request.POST["since"], request.POST["keywords1"],
                                             post.researchId)
        post.executionDuration = time.time() - start_time
        if post.executionDuration == 0.0:
            post.ratio = 0
        else:
            post.ratio = float(post.numberOfTweets / post.executionDuration)
        post.resultsFileName = 'static/collected_data/results_{}.json'.format(post.researchId)
        post.save()
        return post
    else:
        return render(request, 'template1/researchType.html', {'form': form})


def previous(request):
    previousResearches = research.objects.all()
    return render(request, 'template1/previous.html', locals())


def researchChoice(request):
    return render(request, 'template1/researchType.html', locals())
