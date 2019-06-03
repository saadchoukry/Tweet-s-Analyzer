from django.contrib import admin
from search.models import *
import os



def delete_research_json(researchAdmin,request,queryset):
    for obj in queryset:
        if os.path.isfile("static/collected_data/results_{}.json".
                                  format(obj.researchId)):
            os.remove("static/collected_data/results_{}.json".format(obj.researchId))
        obj.delete()


delete_research_json.short_description = "Delete research(es) and collected tweets"



@admin.register(research)
class researchAdmin(admin.ModelAdmin):
    ordering = ('researchDate',)
    search_fields = ['researchId', 'researchDate', 'researchType']
    list_display = ('researchId', 'researchDate','researchType','numberOfNodes')
    actions = [delete_research_json]

    def get_actions(self,request):
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions




@admin.register(researchType)
class researchAdmin(admin.ModelAdmin):
    search_fields = ['researchType']







@admin.register(streamingResearch)
class streamingAdmin(admin.ModelAdmin):
    date_hierarchy = 'researchDate'
    search_fields = ['researchId', 'researchDate', ]
    list_display = ('researchId', 'researchDate', )
    list_filter = ('keywords',)


admin.site.site_header = "Tweets' Analyzer: admin section"
