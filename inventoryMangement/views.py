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
            resp = service.convertRequestToInventoryObject(request.body)
            return HttpResponse(resp)
        else:
            return HttpResponse(constants.AUTH_FAILED)

