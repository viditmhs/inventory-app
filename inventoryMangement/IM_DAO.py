'''
    Author: Vidit Maheshwrai
    Date: 20170205 (YYYYMMDD)
    Copyright :

    Purpose: Contain all DAO to for data base communications

    History:

    Help: http://docs.mongoengine.org/tutorial.html

'''

from mongoengine import *


def addVehicalDAO(vehical):
    try:
        print("[INFO] Connecting DB")
        a = connect('inventoryData')
        print("[INFO] Connection stablished")

        print("[INFO] Inserting new vehical entry in docuent for VIN NUMBER: " + vehical.vn);
        vehical.save()
        print("[INFO] Inserting done from VIN NUMBER: " + vehical.vn)

        print("[INFO] Disconnecting DB")
        #disconnect('inventoryData');

    except Exception as e:

        print("[Error] " + e)