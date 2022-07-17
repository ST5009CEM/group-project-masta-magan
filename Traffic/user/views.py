from django.shortcuts import render, redirect

# Uer Model

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from vechiles.models import CheatModel
from user.froms import UserInfoForm
from vechiles.models import LostModel
from django.contrib.auth.models import User



# Create your views here.
@login_required(login_url='/admin/login')

def home_page(request):
    return render(request,'admin/home.html')

@login_required(login_url='/admin/login')

def calander_page(request):
        return render(request,'admin/calander.html')

@login_required(login_url='/admin/login')

def addprofile_page(request):
        return render(request,'admin/profile.html')

@login_required(login_url='/admin/login')

def next_profilepage(request):
    if request.method == "POST":

        
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']  
        username = request.POST['username']
        password = request.POST['password']  
        email = request.POST['email']
        cpassword = request.POST['confirmpassword']   

        if password==cpassword: 

            User.objects.create_user(
                first_name = f_name,
                last_name = l_name,
                username = username,
                password = password,
                email = email,

            )

            user = User.objects.get(request,username=username,password=password)

            return render(request,'admin/nextprofile.html',{'user',user})
        

    else:
            return redirect("admin/addprofile")

def next(request,id):
    data = UserInfoForm(request.POST, request.FILES)
    data.save()

    return redirect('admin/addprofile')
    



def user_login(request):
    return render(request,'login/adminlogin.html')


@login_required(login_url='/admin/login')

def history_page(request):
        data = CheatModel.objects.all()
        return render(request,'admin/history.html',{'data':data})


@login_required(login_url='/admin/login')

def report_page(request):
    data = LostModel.objects.all().filter(resolved='reported')
    file = LostModel.objects.all().filter(resolved='solved')

    return render(request,'admin/report.html',{'data':data,'file':file})

@login_required(login_url='/admin/login')

def addreport_page(request):
    return render(request,'admin/reportform.html')

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