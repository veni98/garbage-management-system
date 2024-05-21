from django.shortcuts import render
from .models import *

# Create your views here.
def login1(request):
    return render(request,'login.html')

def reg1(request):
    return render(request,'register.html')


def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        name1=request.POST["name"]
        email=request.POST["email"]
        password1=request.POST["password"]
        conform=request.POST["confirm"]
        if password1!=conform:
            return render(request,'register.html',{"key":"password not match"})
        x=logins(name=name1,password=password1)
        x.save()
        user.objects.create(LOGIN=x,Email=email,name=name1)
        return render(request,'login.html')
    else:
        return render(request,'register.html')
    


def login(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        res=logins.objects.filter(name=name,password=password)
        if res.exists():
            return render(request,'home.html')
    return render(request,'login.html')
