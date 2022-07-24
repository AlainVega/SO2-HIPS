from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template 
from django.contrib.auth import authenticate,login
def index(request):
    return render(request,"login.html")
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password    = request.POST['password']
        print(username,password)
        user     = authenticate(username=username , password=password)
        if user is not None:
            print("tumama")
            login(request,user)
            return render(request,"index.html")