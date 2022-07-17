from django.shortcuts import redirect, render
from vechiles.froms import CheatForm
from django.contrib import messages

# Create your views here.

def createcheat(request):
    if request.method == 'POST' :

        data = CheatForm(request.POST)
        data.save()
        return redirect('/cheat')

    else:
        messages.error(request,"Uable to add Product , Please Try Again")
        return redirect('/cheat')  