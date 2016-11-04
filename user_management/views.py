from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# starting page
def start(request):
    return render(request, 'user_management/loginPage.html', "")

def loginStart(request):
    userLoginId = request.POST.get('loginId', '')
    userPass = request.POST.get('loginPass', '')
    if(userLoginId == "admin"):
        if(userPass == "admin"):
            return render(request, 'user_management/loginSuccess.html', {'user_login_id': userLoginId})
        else:
            return render(request, 'user_management/loginUnsuccess.html', {'user_login_id': userLoginId})
    else:
        return render(request, 'user_management/loginfailed.html', {'user_login_id': userLoginId})