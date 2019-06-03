from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from results import views as resultsViews

urlpatterns = [
    path('<research_id>/', resultsViews.results, name='results'),
    path('mapping/<research_id>/', resultsViews.mapping, name='mapping'),
    path('visualization/<research_id>/', resultsViews.visualization, name='visualization'),
    path('advancedStats/',resultsViews.advancedStats,name='advancedStats'),
]

urlpatterns += staticfiles_urlpatterns()

