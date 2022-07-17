from django.shortcuts import render, redirect

# Uer Model

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages




# Create your views here.
@login_required(login_url='/admin/login')

def home_page(request):
    return render(request,'admin/home.html')

@login_required(login_url='/admin/login')

def calander_page(request):
        return render(request,'user/calander.html')

@login_required(login_url='/admin/login')

def addprofile_page(request):
        return render(request,'user/profile.html')



def user_login(request):
    return render(request,'login/adminlogin.html')


@login_required(login_url='/admin/login')

def history_page(request):
        return render(request,'user/history.html')


@login_required(login_url='/admin/login')

def report_page(request):
    return render(request,'user/report.html')


def login_verification(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']    
        
        user = authenticate(request,username=username, password=password)

        if user is not None:
            if user.is_superuser == 1:

                log(request,user)
                return redirect('/admin/home')

            else:
                messages.error(request,"Username and Password Don't Match, Please Try Again !")
                return redirect('/admin/login')        
        else:
            messages.error(request,"Username and Password Don't Match, Please Try Again !")
            return redirect('/admin/login')


    else:
        messages.error(request,"Something is worng with your form validation, Please Try Again !")

        return redirect('admin/login')

  
def log_out(request):
    logout(request)
    return redirect('/admin/login')