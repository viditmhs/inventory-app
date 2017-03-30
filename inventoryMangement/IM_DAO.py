'''
    Author: Vidit Maheshwrai
    Date: 20170205 (YYYYMMDD)
    Copyright :

    Purpose: Contain all DAO to for data base communications

    History:

    Help: http://docs.mongoengine.org/tutorial.html

'''

from mongoengine import *
import json

#
import models as Model


def saveVehicalDAO(vehical):
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


def getVehicalByVinNumber(_vn):
    try:
        print("[INFO] Connecting DB")
        a = connect('inventoryData')
        print("[INFO] Connection stablished")

        vehicalCount = Model.Vehical.objects(vn=_vn)
        print("[Info] Vehical with vn " + _vn + ". Number of entries "+ str(len(vehicalCount)))
        if (len(vehicalCount) > 0):
            return vehicalCount
        else:
            return None

    except Exception as e:
        print ("Error in getVehicalByVinNumber")
        print(e)
        return ""


def getVehicalByChasisNumber(_chasisNumber):
    try:

        print("[INFO] Connecting DB")
        a = connect('inventoryData')
        print("[INFO] Connection stablished")

        vehicalCount = Model.Vehical.objects(chasisNumber=_chasisNumber)
        print("[Info] Vehical with vn " + _chasisNumber + ". Number of entries " + str(len(vehicalCount)))
        if(len(vehicalCount)>0):
            return vehicalCount
        else:
            return None

    except Exception as e:
        print ("Error in getVehicalByChasisNumber")
        print(e)
        return ""

def getVehicalDataDAO(_query):
    try:
        print("[INFO] Connecting DB")
        a = connect('inventoryData')
        print("[INFO] Connection stablished")
        vn = ""
        chasisNumber = ""
        if(_query != ""):
            if('vn' in _query):
                vn = _query['vn']

            if('chasisNumber' in _query):
                chasisNumber = _query['chasisNumber']

        #print(vn)
        #print(chasisNumber)

        if vn != "" and chasisNumber != "":
            resp = Model.Vehical.objects(Q(vn=vn) | Q(chasisNumber=chasisNumber) )
        elif vn != "" :
            resp = Model.Vehical.objects(Q(vn=vn))
        elif chasisNumber != "":
            resp = Model.Vehical.objects(Q(chasisNumber=chasisNumber))
        elif _query == "":
            resp = Model.Vehical.objects()
        else:
            resp = {}
            resp['message']  = "Invalid request."

        return resp


    except Exception as e:
        print ("Error in getVehical " + json.dumps(_query))
        print(e)
        return ""