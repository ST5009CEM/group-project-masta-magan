from django.shortcuts import redirect, render
from vechiles.froms import CheatForm, LostForm
from django.contrib import messages

from vechiles.models  import LostModel

# Create your views here.

def createcheat(request):
    if request.method == 'POST' :

        data = CheatForm(request.POST)
        data.save()
        return redirect('/cheat')

    else:
        messages.error(request,"Uable to create cheat , Please Try Again")
        return redirect('/cheat')  

def report(request):
    if request.method == 'POST' :

        data = LostForm(request.POST)
        data.save()
        return redirect('/report')

    else:
        messages.error(request,"Uable to add report , Please Try Again")
        return redirect('/report')  


def admin_report(request):
    if request.method == 'POST' :

        data = LostForm(request.POST)
        data.save()
        return redirect('/admin/report')

    else:
        messages.error(request,"Uable to add report , Please Try Again")

def found(request,id):
    data = LostModel.objects.get(id=id)
    data.resolved = 'solved'
    data.save()

    return redirect('/report')

