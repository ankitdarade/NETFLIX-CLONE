from django.contrib.auth import login,authenticate
from .models import home
from .forms import Companymaster
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def CreatecompanyNew(request):
    ddlcompanyobjects = home.ddlcompanyobjects.all()

    if request.method == 'POST':
        form = Companymaster(request.POST)
        print(form.errors, form)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return render(request, 'index.html', {'form': form, 'ddlcompanyobjects': ddlcompanyobjects})
    else:
        form = Companymaster()
    return render(request, 'index.html', {'form': form, 'ddlcompanyobjects': ddlcompanyobjects})

def homepage(request):
    return render(request,'index.html')

def signinpage(request):
    return render(request,'signin.html')

def signuppage(request):
    return render(request,'signup.html')

def firstpage(request):
    return render(request,'1st.html')
