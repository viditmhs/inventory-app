# for connecting dataBase
from pymongo import MongoClient

from pymongo.son_manipulator import SONManipulator
from models import User

DB = 'im'

def mongoConnect():
    client = MongoClient()
    im = client.im
    return im
