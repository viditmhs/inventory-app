from django.shortcuts import render
from django.http import HttpResponse

from django.core import serializers

# importing models
import ErrorResponseMessage as erm
import UserServiceController as usc
# Create your views here.

# starting page
def start(request):
    return render(request, 'user_management/loginPage.html', '')

def loginStart(request):
    userLoginId = request.POST.get('loginId', '')
    userPass = request.POST.get('loginPass', '')
    u = usc.getUserByEmail(userLoginId)
    print(u.toJSON())
    if(u is not None and userLoginId == u.email):
        if(userPass == u.password):
            
            return render(request, 'user_management/loginSuccess.html', {'user_login_id': u.first_name + " " + u.last_name})
        else:
            return HttpResponse(erm.createRC_RM('400', 'Incorrect password'), content_type='application/json')
    else:
        return HttpResponse(erm.createRC_RM('400','Invalid user'), content_type='application/json')