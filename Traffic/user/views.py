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


from user.models import UserInfoModel


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
            user = authenticate(request,username=username, password=password)
            if user is not None:

                uid = user.id 

                id={
                    'uid': uid
                    
                }
            
                return render(request,'admin/nextprofile.html',{"id":id})
        

    else:
            return redirect("admin/addprofile")

def next(request,id):
    if request.method == "POST":

        
        title = request.POST['title']
        badge = request.POST['badge']  
        date = request.POST['date']
        description = request.POST['description']  
        section = request.POST['section']
        age = request.POST['age'] 

        role = request.POST['role']
        contact = request.POST['contact']  
        area = request.POST['area']
        address = request.POST['address']  
        medals = request.POST['medals']
        solvedcases = request.POST['solvedcases'] 

        badges = request.POST['badges']
        cheat = request.POST['cheat'] 

        profile_image  = request.FILES.get('profile_image')


        UserInfoModel.objects.create(uid=id,title=title,badge=badge,date=date,description=description,section=section,age=age,role=role,contact=contact,area=area,address=address,medals=medals,solvedcases=solvedcases,badges=badges,cheat=cheat,profile_image=profile_image)

        return redirect('/admin/addprofile')
    



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