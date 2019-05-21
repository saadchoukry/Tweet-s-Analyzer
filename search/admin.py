from django.contrib import admin
from search.models import *





@admin.register(researchType)
class researchAdmin(admin.ModelAdmin):
    search_fields = ['researchType']




@admin.register(research)
class researchAdmin(admin.ModelAdmin):
    date_hierarchy = 'researchDate'
    search_fields = ['researchId', 'researchDate', 'researchType']
    list_display = ('researchId', 'researchDate','researchType','numberOfNodes')


@admin.register(streamingResearch)
class streamingAdmin(admin.ModelAdmin):
    date_hierarchy = 'researchDate'
    search_fields = ['researchId', 'researchDate', ]
    list_display = ('researchId', 'researchDate', )
    list_filter = ('keywords',)

"""
@admin.register(ByHashtags)
class hashtagsAdmin(admin.ModelAdmin):
    date_hierarchy = 'researchDate'
    search_fields = ['researchId', 'researchDate', 'hashtags']
    list_display = ('researchId', 'researchDate', 'hashtags')
    list_filter = ('hashtags',)


@admin.register(ByKeywords)
class keywordsAdmin(admin.ModelAdmin):
    date_hierarchy = 'researchDate'
    search_fields = ['researchId', 'researchDate', 'keywords']
    list_display = ('researchId', 'researchDate', 'keywords')
    list_filter = ('keywords',)


@admin.register(ByScreenName)
class screenNameAdmin(admin.ModelAdmin):
    date_hierarchy = 'researchDate'
    search_fields = ['researchId', 'researchDate', 'screenName']
    list_display = ('researchId', 'researchDate', 'screenName')
    list_filter = ('screenName',)

"""
admin.site.site_header = "Tweets' Analyzer: admin section"
