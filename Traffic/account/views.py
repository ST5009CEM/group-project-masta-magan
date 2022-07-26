from django.shortcuts import render, redirect

# Uer Model

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from vechiles.models import CheatModel, LostModel
from user.models import UserInfoModel


# Create your views here.
@login_required(login_url='/login')

def home_page(request):
    return render(request,'user/home.html')

@login_required(login_url='/login')

def calander_page(request):
        return render(request,'user/calander.html')

@login_required(login_url='/login')

def profile_page(request,id):
        data = UserInfoModel.objects.get(uid=id)
        return render(request,'user/profile.html',{'data':data})



def user_login(request):
    return render(request,'login/userlogin.html')

@login_required(login_url='/login')

def token_page(request):
        return render(request,'user/cheat.html')

def create_cheat(request):
        return render(request,'user/cheatForm.html')

@login_required(login_url='/login')

def history_page(request):
        data = CheatModel.objects.all()
        return render(request,'user/history.html',{'data':data})


@login_required(login_url='/login')

def report_page(request):
    data = LostModel.objects.all().filter(resolved='reported')
    file = LostModel.objects.all().filter(resolved='solved')

    return render(request,'user/report.html',{'data':data,'file':file})

@login_required(login_url='/login')

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
  
def log_out(request):
    logout(request)
    return redirect('/login')
