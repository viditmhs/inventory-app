from django.shortcuts import render
from django.http import HttpResponse

# importing models
from models import User
from dbService import mongoConnect as mc
# Create your views here.

# starting page
def start(request):
    return render(request, 'user_management/loginPage.html', '')

def loginStart(request):
    userLoginId = request.POST.get('loginId', '')
    userPass = request.POST.get('loginPass', '')
    user = User()
    u = user.convert(mc().User.find_one({"email" : userLoginId}))

    if(u is not None and userLoginId == u.email):
        if(userPass == u.password):
            return render(request, 'user_management/loginSuccess.html', {'user_login_id': userLoginId})
        else:
            return render(request, 'user_management/loginUnsuccess.html', {'user_login_id': userLoginId})
    else:
        return render(request, 'user_management/loginfailed.html', {'user_login_id': userLoginId})