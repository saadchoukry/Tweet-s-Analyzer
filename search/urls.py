from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from search import views as searchViews
urlpatterns =[
    path('',searchViews.search,name='search'),
    path('uploadTweets/',searchViews.uploadTweets,name='uploadTweets'),
    path('previousResearches/',searchViews.previous, name='PreviousResearches'),
    ]

urlpatterns += staticfiles_urlpatterns()