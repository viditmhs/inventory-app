from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.

# User model created here

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=100)
    last_name = StringField(max_length=100)
    role = ListField()
    password = StringField(max_length=100)

    def convert(self, document):
        if(document is not None):
            return User(document['email'], document['first_name'], document['last_name'], document['role'],
                        document['password'])
        else:
            return None