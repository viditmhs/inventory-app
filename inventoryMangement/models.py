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

class ServiceData(EmbeddedDocument):
    created = DateTimeField()
    KMstand = IntField()
    itemListReplaced = ListField()
    comment = StringField(max_length=500)
    cost = FloatField()

    def toDATA(self):
        data = {}
        data["created"] = self.created.strftime('%Y-%m-%d %H:%M')
        data["KMstand"] = self.KMstand
        data["itemListReplaced"] = self.itemListReplaced
        data["comment"] = self.comment
        data["cost"] = self.cost
        return data

    def convert(self,document):
        if(document is not None):
            return ServiceData(document['created'],document['KMstand'],document['itemListReplaced'],document['comment'],document['cost'])
        else:
            return None

    def setData(self, _created, _KMstand, _itemListReplaced, _comment, _cost):
        self.created = _created
        self.KMstand = _KMstand
        self.itemListReplaced = _itemListReplaced
        self.comment = _comment
        self.cost = _cost

class TripDetail(EmbeddedDocument):
    tripFrom = StringField(max_lenght=1024)
    tripTo = StringField(max_lenght=1024)
    revenueGenerated = FloatField()
    runningCost = FloatField()
    journeyDuration = StringField(max_lenght=1024);
    journeyDate = DateTimeField();
    odoMeasure = IntField()

    def toDATA(self):
        data = {}
        data["tripFrom"] = self.tripFrom
        data["tripTo"] = self.tripTo
        data["revenueGenerated"] = self.revenueGenerated
        data["runningCost"] = self.runningCost
        data["journeyDuration"] = self.journeyDuration
        data["journeyDate"] = self.journeyDate.strftime('%Y-%m-%d %H:%M')
        data["odoMeasure"] = self.odoMeasure

        return data

    def setData(self, _tripFrom, _tripTo, _revenueGenerated, _runningCost, _journeyDuration, _journeyDate, _odoMeasure):
        self.tripFrom = _tripFrom
        self.tripTo = _tripTo
        self.revenueGenerated = _revenueGenerated
        self.runningCost = _runningCost
        self.journeyDuration = _journeyDuration
        self.journeyDate = _journeyDate
        self.odoMeasure = _odoMeasure

class Vehical(Document):
    purchaseDate = DateTimeField()
    vn = StringField(max_length=20)
    chasisNumber = StringField(max_length=20)
    serviceHistory = EmbeddedDocumentListField(ServiceData)
    tripHistory = EmbeddedDocumentListField(TripDetail)

    def toJSON(self):
        data = {}
        data["purchaseDate"] = self.purchaseDate.strftime('%Y-%m-%d %H:%M')
        data["vn"] = self.vn
        data["chasisNumber"] = self.chasisNumber
        if(len(self.serviceHistory)>0):
            sHistory = []
            for s in self.serviceHistory:
                sHistory.append(s.toDATA())
            data["serviceHistory"] = sHistory
        else:
            data["serviceHistory"] = "[]"

        if(len(self.tripHistory)>0):
            trips = []
            for trip in self.tripHistory:
                trips.append(trip.toDATA())
            data["tripHistory"] = trips
        else:
            data["tripHistory"] = "[]"

        return json.dumps(data)