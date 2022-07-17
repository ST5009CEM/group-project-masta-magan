from django.shortcuts import render, redirect

# Uer Model

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout

from vechiles.models import CheatModel, LostModel


# Create your views here.

def home_page(request):
    return render(request,'user/home.html')

def calander_page(request):
        return render(request,'user/calander.html')

def profile_page(request):
        return render(request,'user/profile.html')



def user_login(request):
    return render(request,'user/login.html')

def token_page(request):
        return render(request,'user/cheat.html')

def create_cheat(request):
        return render(request,'user/cheatForm.html')

def history_page(request):
        data = CheatModel.objects.all()
        return render(request,'user/history.html',{'data':data})



def report_page(request):
    data = LostModel.objects.all()
    return render(request,'user/report.html',{'data':data})

def addreport_page(request):
    return render(request,'user/reportform.html')


def login_verification(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username, password=password)

        if user is not None:
            log(request,user)
            return redirect('/home')

        else:
            return render(request, '404.html', status=404)
  
