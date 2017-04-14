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
        _tripHistory = {}
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
        vehical.tripHistory = _tripHistory
        vehical.serviceHistory = _serviceHistory

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
            return vehicals[0].toJSON()
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
        if(vehical is not None):
            ## Validate input request
            tripData = getTripDataFromRequest(jObject)
            if(tripData is not None):
                vehical.update(add_to_set__tripHistory=tripData )
                return "Successfully Added Trip"
            else:
                resp['code'] = "203"
                resp['message'] = "Illegal Trip Data"
                return json.dumps(resp)
        else:
            resp['code'] = "203"
            resp['message'] = "Vehical Not In System."
            return json.dumps(resp)

        # Add new trip data
        ## check for valid trip data
        ## validate trip data from previous trip data


    except json.JSONDecoder as e:
        print(e)
        resp = "Invalid JSON request"
        return resp

    return "Application Error"

def addService(req):
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
        if(vehical is not None):
            ## Validate input request
            serviceData = getServiceDataFromRequest(jObject)
            if(serviceData is not None):
                vehical.update(add_to_set__serviceHistory=serviceData )
                return "Successfully Added Service"
            else:
                resp['code'] = "203"
                resp['message'] = "Illegal Trip Data"
                return json.dumps(resp)
        else:
            resp['code'] = "203"
            resp['message'] = "Vehical Not In System."
            return json.dumps(resp)

        # Add new trip data
        ## check for valid trip data
        ## validate trip data from previous trip data


    except json.JSONDecoder as e:
        print(e)
        resp = "Invalid JSON request"
        return resp

    return "Application Error"

def getTripDataFromRequest(jObject):
    if("trip" not in jObject):
        return None
    else:
        tripData = jObject["trip"]
        trip = Models.TripDetail();
        trip.setData(tripData["tripFrom"], tripData["tripTo"], tripData["revenueGenerated"], tripData["runningCost"],
                     tripData["journeyDuration"],tripData["journeyDate"],tripData["odoMeasure"])
        return trip;

def getServiceDataFromRequest(jObject):
    if("service" not in jObject):
        return None
    else:
        serviceData = jObject["service"]
        service = Models.ServiceData();
        service.setData(serviceData["created"], serviceData["KMstand"], serviceData["itemListReplaced"], serviceData["comment"],
                        serviceData["cost"])
        return service;

def getVehicalServiceData(req):
    resp = ""
    try:
        print(req)
        if(req == ""):
            jObject = "";
        else:
            jObject = json.loads(req)
            vehicals = dao.getVehicalDataDAO(jObject)
            resp = {}
            resp["ServiceHistory"] = json.loads(vehicals[0].toJSON())["serviceHistory"]
            return json.dumps(resp)
    except json.JSONDecoder as e:
        print(e)
        resp = "Invalid JSON request"

    return resp

def getVehicalTripData(req):
    resp = ""
    try:
        print(req)
        if(req == ""):
            jObject = "";
        else:
            jObject = json.loads(req)
            vehicals = dao.getVehicalDataDAO(jObject)
            resp = {}
            resp["TripHistory"] = json.loads(vehicals[0].toJSON())["tripHistory"]
            return json.dumps(resp)
    except json.JSONDecoder as e:
        print(e)
        resp = "Invalid JSON request"

    return resp
