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

def saveVehical(data):
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

        #Check if vehical with given vn and chasisNumber already present
        if(dao.getVehicalByVinNumber(_vn) != None):
            return "Error: Vehical with vn=" + _vn + " already exist."
        if (dao.getVehicalByChasisNumber(_chasisNumber) != None):
            return "Error: Vehical with chasisNumber=" + _chasisNumber + " already exist."

        vehical = Models.Vehical();
        vehical.purchaseDate = _purchaseDate
        vehical.vn = _vn
        vehical.chasisNumber = _chasisNumber
        vehical.dailyUpdate = _dailyUpdate
        vehical.serviceHistory = _serviceHistory;

        #Making connection to DB

        dao.saveVehicalDAO(vehical)

        return "Success:" + "done"
    except KeyError as e:

        return "Error:"  + constants.MALFORMED_DATA;

    except Exception as e:
        print(e)
        return "[Error] : "

def getVehicalData(req):
    resp = ""
    try:
        print(req)
        if(req == ""):
            jObject = "";
        else:
            jObject = json.loads(req)
            vehicals = dao.getVehicalDataDAO(jObject)
        return vehicals[0].toJSON();
    except json.JSONDecoder as e:
        print(e)
        resp = "Invalid JSON request"

    return resp

def addTrip(req):
    try:
        print(req)
        jObject = json.loads(req)
        resp = {}
        # Get vehical information
        ## Check if valid vn is given
        vn = "";
        if('vn' not in jObject):
            resp['code'] = "400"
            resp['message']="Missing vn."
            return json.dumps(resp)
        else:
            vn = jObject['vn']

        ## Check for given vn we have vehical in the database
        _query = {}
        _query["vn"] = vn
        vehical = dao.getVehicalDataDAO(_query)
        print (vehical)
        return "Got Vehical"

        # Add new trip data
        ## check for valid trip data
        ## validate trip data from previous trip data


    except json.JSONDecoder as e:
        print(e)
        resp = "Invalid JSON request"
        return resp

    return "NOT IMPLEMENTED"