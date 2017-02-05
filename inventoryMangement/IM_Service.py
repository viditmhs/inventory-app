'''
    Author: Vidit Maheshwrai
    Date: 20170204 (YYYYMMDD)
    Copyright :

    Purpose: This service communicate between DB

    History:

'''

# dependencies

import json

# Local app imports
import models as Models
import IM_Constants as  constants
import IM_DAO as dao

def convertRequestToInventoryObject(data):
    vehical = Models.Vehical
    jObject = json.loads(data)
    try:

        # TODO:
        # 1: Check if given documnet alsready exists
        # 2: Check if parameters are missing
        # 3: Othr validation

        _purchaseDate = jObject['purchanseDate']
        _vn = jObject['vn']
        _chasisNumber = jObject['chasisNumber']
        _dailyUpdate = {}
        _serviceHistory = {}

        vehical = Models.Vehical();
        vehical.purchaseDate = _purchaseDate
        vehical.vn = _vn
        vehical.chasisNumber = _chasisNumber
        vehical.dailyUpdate = _dailyUpdate
        vehical.serviceHistory = _serviceHistory;

        #Making connection to DB

        dao.addVehicalDAO(vehical)

        return "Success:" + "done"
    except KeyError as e:

        return "Error:"  + constants.MALFORMED_DATA;

    except Exception as e:

        print("[Error] : " + e)