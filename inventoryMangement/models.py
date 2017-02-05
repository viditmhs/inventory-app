from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.


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

class ServiceHistory(Document):
    created = DateTimeField()
    KMstand = IntField()
    itemListReplaced = ListField()
    comment = StringField(max_length=500)
    cost = FloatField()

    def convert(self,document):
        if(document is not None):
            return ServiceHistory(document['created'],document['KMstand'],document['itemListReplaced'],document['comment'],document['cost'])
        else:
            return None

class Vehical(Document):
    purchaseDate = DateTimeField()
    vn = StringField(max_length=20)
    chasisNumber = StringField(max_length=20)
    dailyUpdate = {}
    serviceHistory = {}

    def convert(self, document):

        if(document is not None):
            return Vehical(document['purchaseDate'],document['vn'],document['chasisNumber'],document['dailyUpdate'],document['serviceHistory'])
        else:
            return None