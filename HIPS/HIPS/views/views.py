
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password    = request.POST['password']
        print(username,password)
        user     = authenticate(username=username , password=password)
        if user is not None:
            login(request,user)
            return render(request,"index.html")
        
    return render(request, "login.html")
