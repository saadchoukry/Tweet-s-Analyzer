import pycountry
from geopy import Nominatim

from JsonParser import get_json
from search.models import research as R


class countryToALpha3:
    def __init__(self, research_id):
        self.locations = []
        research = R.getResearchById(research_id)
        for tweet in get_json(research):
            if str(tweet["user"]["location"]) != "None":
                self.locations.append(tweet["user"]["location"])
        self.countries = []
        self.alpha2Countries = []
        self.alpha3Countries = []
        self.countryCounter = {}
        self.total = 0
        self.file = open('static/collected_coutries', 'w')

    def getAlpha2Countries(self):
        geolocator = Nominatim(timeout=60)
        for location in self.locations:
            geo = geolocator.geocode(location)
            if geo is not None:
                loc = geolocator.reverse("{}, {}".format(geo.latitude, geo.longitude))
                self.alpha2Countries.append(loc.raw['address']['country_code'].upper())

    def getAlpha3Countries(self):
        for alpha2country in self.alpha2Countries:
            c = pycountry.countries.get(alpha_2=alpha2country)
            if c is not None:
                self.alpha3Countries.append(c.alpha_3)

    def getCountryCount(self):
        for alpha3Country in self.alpha3Countries:
            self.total += 1
            if alpha3Country in self.countryCounter:
                self.countryCounter[alpha3Country]["numberOfThings"] += 1
            else:
                self.countryCounter[alpha3Country] = {"fillKey": None, "numberOfThings": 1}

    def updateFillKeys(self):
        for country in self.countryCounter.values():
            if country["numberOfThings"] / self.total >= 0.6:
                country["fillKey"] = "HIGH"
            if (country["numberOfThings"] / self.total < 0.6) \
                    and (country["numberOfThings"] / self.total > 0.10):
                country["fillKey"] = "MEDIUM"
            if country["numberOfThings"] / self.total < 0.10:
                country["fillKey"] = "LOW"
