from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template 
def index(request):
    template = get_template('login.html')
    return HttpResponse(template.render())