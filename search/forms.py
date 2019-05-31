from datetime import date

from django import forms
from search.models import streamingResearch, ByScreenName, ByHashtags, ByKeywords, uploadedTweets


class streamingForm(forms.ModelForm):
    class Meta:
        model = streamingResearch
        fields = ['streamingDuration', 'keywords']

    def clean(self):
        super(streamingForm, self).clean()
        streamingDuration = self.cleaned_data.get('streamingDuration')
        keywords = self.cleaned_data.get('keywords')

        if streamingDuration is not None:

            if streamingDuration > 60:
                self._errors['streamingDuration'] = self.error_class([
                    'Streaming duration must not be greater than 60 seconds .'])

            if streamingDuration < 1:
                self.errors['streamingDuration'] = self.error_class([
                    'Streaming duration must be equal or greater than 1 second .'
                ])

        else:
            self.errors['streamingDuration'] = self.error_class([
                'Streaming duration must be set .'
            ])

        if len(keywords) == 0:
            self._errors['keywords'] = self.error_class([
                'Please enter your chosen keywords'])

        return self.cleaned_data


class byScreenNameForm(forms.ModelForm):
    class Meta:
        model = ByScreenName
        fields = ['screen', 'count', 'since']

    def clean(self):
        super(byScreenNameForm, self).clean()
        count = self.cleaned_data.get('count')
        since = self.cleaned_data.get('since')
        screen = self.cleaned_data.get('screen')

        if count is not None:

            if count > 500:
                self._errors['count'] = self.error_class([
                    'The number of tweets must not be greater than 500.'])

            if count < 1:
                self.errors['count'] = self.error_class([
                    'The number of tweets must be equal or greater than 1.'
                ])

        else:
            self.errors['count'] = self.error_class([
                'The limit number of tweets must be set .'
            ])

        if screen == "":
            self._errors['screen'] = self.error_class([
                'Please enter your chosen screen name'])

        if since is not None:
            if since > date.today():
                self._errors['since'] = self.error_class([
                    'Sorry but we can\'t extract future tweets'])
        else:
            self._errors['since'] = self.error_class([
                'Since Date must be set .'])

        return self.cleaned_data


class byHashtagForm(forms.ModelForm):
    class Meta:
        model = ByHashtags
        fields = ['tag', 'count', 'since']

    def clean(self):
        super(byHashtagForm, self).clean()
        count = self.cleaned_data.get('count')
        since = self.cleaned_data.get('since')
        tag = self.cleaned_data.get('tag')
        print(tag)
        if count is not None:

            if count > 500:
                self._errors['count'] = self.error_class([
                    'The number of tweets must not be greater than 500.'])

            if count < 1:
                self.errors['count'] = self.error_class([
                    'The number of tweets must be equal or greater than 1.'
                ])

        else:
            self.errors['count'] = self.error_class([
                'The limit number of tweets must be set .'
            ])

        if tag == "":
            self._errors['tag'] = self.error_class([
                'Please enter your chosen hashtag'])

        if since is not None:
            if since > date.today():
                self._errors['since'] = self.error_class([
                    'Sorry but we can\'t extract future tweets'])
        else:
            self._errors['since'] = self.error_class([
                'Since Date must be set .'])
        return self.cleaned_data


class byKeywordsForm(forms.ModelForm):
    class Meta:
        model = ByKeywords
        fields = ['keywords1', 'count', 'since']

    def clean(self):
        super(byKeywordsForm, self).clean()
        count = self.cleaned_data.get('count')
        since = self.cleaned_data.get('since')
        keywords = self.cleaned_data.get('keywords1')

        if count is not None:

            if count > 500:
                self._errors['count'] = self.error_class([
                    'The number of tweets must not be greater than 500.'])

            if count < 1:
                self.errors['count'] = self.error_class([
                    'The number of tweets must be equal or greater than 1.'
                ])

        else:
            self.errors['count'] = self.error_class([
                'The limit number of tweets must be set .'
            ])

        if keywords == "":
            self._errors['keywords1'] = self.error_class([
                'Please enter your chosen keywords'])

        if since is not None:
            if since > date.today():
                self._errors['since'] = self.error_class([
                    'Sorry but we can\'t extract future tweets'])
        else:
            self._errors['since'] = self.error_class([
                'Since Date must be set .'])
        return self.cleaned_data


class uploadForm(forms.ModelForm):
    class Meta:
        model = uploadedTweets
        fields = ['jsonFile', 'description']

    def clean(self):
        super(uploadForm, self).clean()
        jsonFile = self.cleaned_data.get('jsonFile')
        description = self.cleaned_data.get('description')

        if jsonFile is None:
            self.errors['jsonFile'] = self.error_class([
                'You must include a json file .'
            ])

        if description is None:
            self.errors['description'] = self.error_class([
                'A description is needed .'])
        return self.cleaned_data
