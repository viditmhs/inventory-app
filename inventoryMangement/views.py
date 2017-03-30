from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Application imports

import IM_Utility as util
import IM_Constants as constants
import IM_Service as service

# Other Application imports

# Create your views here.
@csrf_exempt
def add(request):
    print("[INFO] Adding new vehical entry.")
    if request.method == 'GET':
        return HttpResponse("GET request not accepted.")
    elif request.method == 'POST':
        if(util.authentication(request.META['HTTP_AUTH'])):
            resp = service.saveVehical(request.body)
            return HttpResponse(resp)
        else:
            return HttpResponse(constants.AUTH_FAILED)
    else:
        return HttpResponse("Invalid request.")

@csrf_exempt
def get(request):
    print("[INFO] Request to get all vehical data")
    if request.method == 'GET':
        return HttpResponse("GET request not accepted")
    elif request.method == 'POST':
        if (util.authentication(request.META['HTTP_AUTH'])):
            resp = service.getVehicalData(request.body)
            return HttpResponse(resp)
    else:
        return HttpResponse("Invalid request")

@csrf_exempt
def appendTrip(request):
    print("[INFO] Request to add trip received.")
    if request.method == 'GET':
        return HttpResponse("GET request not accepted")
    elif request.method == 'POST':
        if (util.authentication(request.META['HTTP_AUTH'])):
            resp = service.addTrip(request.body)
            return HttpResponse(resp)
    else:
        return HttpResponse("Invalid request")


