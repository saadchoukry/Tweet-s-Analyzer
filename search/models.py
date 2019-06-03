from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone


class researchType(models.Model):
    researchTypes = (('Stream', 'Stream'), ('OffStream', 'OffStream'), ('Upload', 'Upload'))
    type = models.CharField(default='Stream', choices=researchTypes, max_length=10)

    class Meta:
        verbose_name = 'Research Type'

    def __str__(self):
        return 'Type : {}'.format(self.type)


class research(models.Model):
    researchId = models.AutoField(primary_key=True)
    researchType = models.ForeignKey(researchType, on_delete=models.CASCADE, null=True)
    researchDate = models.DateTimeField(default=timezone.now())
    numberOfTweets = models.IntegerField(default=0)
    ratio = models.IntegerField(default=0)
    resultsFileName = models.TextField(default='static/collected_data/default.json')
    numberOfNodes = models.IntegerField(default=0)
    executionDuration = models.FloatField(default=0)

    @staticmethod
    def getResearchById(id):
        return research.objects.get(researchId=id)

    @property
    def getKeywords(self):
        streamingresearch = streamingResearch.objects.get(researchId=self.researchId)
        return streamingresearch.keywords

    @property
    def getScreenName(self):
        researchByScreenName = ByScreenName.objects.get(researchId=self.researchId)
        return researchByScreenName.screen

    @property
    def getKeywords2(self):
        researchByKeywords = ByKeywords.objects.get(researchId=self.researchId)
        return researchByKeywords.keywords1

    @property
    def getHashtags(self):
        researchByHashtags = ByHashtags.objects.get(researchId=self.researchId)
        return researchByHashtags.tag

    @property
    def getStreamingDuration(self):
        streamSearch = streamingResearch.objects.get(researchId=self.researchId)
        return streamSearch.streamingDuration

    @property
    def getSince(self):
        offstrSearch = offStreamResearch.objects.get(researchId=self.researchId)
        return offstrSearch.since

    def getCount(self):
        offstrSearch = offStreamResearch.objects.get(researchId=self.researchId)
        return offstrSearch.count

    def getDescription(self):
        upload = uploadedTweets.objects.get(researchId=self.researchId)
        return upload.description

    class Meta:
        verbose_name = "Research"
        verbose_name_plural = "Researches"
        ordering = ["-researchDate"]


class uploadedTweets(research):
    jsonFile = models.FileField(upload_to='static/uploaded_data/', max_length=100, default='')
    description = models.TextField(default='')


class streamingResearch(research):
    keywords = models.TextField(max_length=100, blank=True)
    streamingDuration = models.IntegerField(default=5, blank=True)

    @staticmethod
    class Meta:
        verbose_name = "Streaming research"
        verbose_name_plural = "Streaming researches"

    def __str__(self):
        return self.keywords + "  " + str(self.researchDate)

    @staticmethod
    def getResearchById(id):
        return streamingResearch.objects.get(researchId=id)


class offStreamResearch(research):
    since = models.DateField(default=timezone.now(), blank=True)
    count = models.IntegerField(default=0, blank=True)


class ByScreenName(offStreamResearch):
    screen = models.TextField(default=" ", max_length=100, blank=True)

    class Meta:
        verbose_name = "Research by screen name"
        verbose_name_plural = "Researches by screen name"

    def __str__(self):
        return self.screen + "  " + str(self.researchDate)


class ByHashtags(offStreamResearch):
    tag = models.TextField(default="", max_length=100, blank=True)

    class Meta:
        verbose_name = "Research by hashtags"
        verbose_name_plural = "Researches by hashtags"

    def __str__(self):
        return self.tag + "  " + str(self.researchDate)


class ByKeywords(offStreamResearch):
    keywords1 = models.TextField(default="", max_length=100, blank=True)

    class Meta:
        verbose_name = "Research by keywords"
        verbose_name_plural = "Researches by keywords"

    def __str__(self):
        return self.keywords1 + "  " + str(self.researchDate)


class stats:

    @staticmethod
    def getNumberOfResearches():
        allResearchesNumber = 0
        for resrch in research.objects.all():
            allResearchesNumber += 1
        return allResearchesNumber

    @staticmethod
    def getNumberOfTweets():
        allTweetsNumber = 0
        for resrch in research.objects.all():
            allTweetsNumber += resrch.numberOfTweets
        return allTweetsNumber

    @staticmethod
    def getNumberOfNodes():
        allNodesNumber = 0
        for resrch in research.objects.all():
            allNodesNumber += resrch.numberOfNodes
        return allNodesNumber
