from django import forms
from search.models import streamingResearch, ByScreenName, ByHashtags, ByKeywords


class streamingForm(forms.ModelForm):
    class Meta:
        model = streamingResearch
        fields = ['streamingDuration', 'keywords']


class byScreenNameForm(forms.ModelForm):
    class Meta:
        model = ByScreenName
        fields = ['screen','count','since']

class byHashtagForm(forms.ModelForm):
    class Meta:
        model = ByHashtags
        fields= ['tag','count','since']


class byKeywordsForm(forms.ModelForm):
    class Meta:
        model = ByKeywords
        fields= ['keywords','count','since']
