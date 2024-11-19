from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
# Create your views here.


def login(request):
    error_msg=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        usere = authenticate(request, username=username, password=password)
        if usere:
            auth_login(request,usere)
            return redirect('list') 
           
        else:
            error_msg='invalid data'
    return render(request,'user/login.html',{'error_msg':error_msg})


def logout(request):
    auth_logout(request)
    return redirect('login')

def signup(request):
    user=None
    error_msg=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.create_user(username=username,password=password)
        except Exception as e:
            error_msg=str(e)

    return render(request,'user/create.html',{'user':user, 'error_msg':error_msg})

