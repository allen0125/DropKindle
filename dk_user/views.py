from django.shortcuts import render, redirect
from dk_user.models import DKUser
from django.contrib import auth
from django.http import HttpResponse

# Create your views here.

def dk_index(request):
    if request.method == 'GET':
        # if request.user.is_authenticated:
        return render(request,'login/index.html')
        # else:
        #     return redirect("/login/")
    if request.method == 'POST':
        pass


def dk_login(request):
    if request.method == 'GET':
        return render(request,'login/login.html')
    if request.method == 'POST':
        _username = request.POST.get('username')
        _password = request.POST.get('password')
        if _username and _password:
            user=auth.authenticate(username=_username,password=_password)
            if user:
                auth.login(request,user)
                return redirect("/")
            else:
                return HttpResponse("用户名或密码错误")


def dk_register(request):
    if request.method == 'GET':
        return render(request,'login/register.html')
    if request.method == 'POST':
        _username = request.POST.get('username')
        _email = request.POST.get('email')
        _password = request.POST.get('password')
        _repassword = request.POST.get('repassword')
        print(_username, _email, _password)
        if _username and _email and _password and _password == _repassword:
            print(_username, _email, _password)
            DKUser.objects.create_user(username=_username, email=_email, password=_password)
            return redirect("/login/")
        return render(request,'login/register.html')


def dk_logout(request):
    auth.logout(request)
    return redirect("/")
