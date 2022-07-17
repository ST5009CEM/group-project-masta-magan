from django.shortcuts import redirect, render
from vechiles.froms import CheatForm, LostForm
from django.contrib import messages

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