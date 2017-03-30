from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.
import json


class DailyUpdate(Document):
    opratorName = StringField(max_length=100)
    startKM = IntField()
    endKM = IntField()
    date = DateTimeField()
    operatorId = StringField(max_length=10)
    serviceHour = StringField(max_length=5)

    def convert(self,document):
        if(document is not None):
            return DailyUpdate(document['opratorName'],document['startKM'],document['endKM'],document['date'],document['operatorId'],document['serviceHour'])
        else:
            return None

class ServiceHistory(EmbeddedDocument):
    created = DateTimeField()
    KMstand = IntField()
    itemListReplaced = ListField()
    comment = StringField(max_length=500)
    cost = FloatField()

    def toJSON(self):
        data = {}
        return json.dumps(data)

    def convert(self,document):
        if(document is not None):
            return ServiceHistory(document['created'],document['KMstand'],document['itemListReplaced'],document['comment'],document['cost'])
        else:
            return None

class TripDetail(EmbeddedDocument):
    tripFrom = StringField(max_lenght=1024)
    tripTo = StringField(max_lenght=1024)
    revenueGenerated = FloatField()
    runningCost = FloatField()
    journeyDuration = StringField(max_lenght=1024);
    journeyDate = StringField(max_lenght=1024);
    odoMeasure = IntField()

    def toJSON(self):
        data = {}
        return json.dumps(data)

class Vehical(Document):
    purchaseDate = DateTimeField()
    vn = StringField(max_length=20)
    chasisNumber = StringField(max_length=20)
    serviceHistory = ListField(EmbeddedDocumentListField(ServiceHistory))
    triphistory = ListField(EmbeddedDocumentListField(TripDetail))

    def toJSON(self):
        data = {}
        data["purchaseDate"] = self.purchaseDate.strftime('%Y-%m-%d %H:%M')
        data["vn"] = self.vn
        data["chasisNumber"] = self.chasisNumber
        data["serviceHistory"] = "{}" #self.serviceHistory.toJSON()
        data["triphistory"] = "{}"#self.triphistory.toJSON()

        return json.dumps(data)