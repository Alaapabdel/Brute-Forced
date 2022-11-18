from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from django.db import connection
from .models import User
import js2py

# Create your views here.
def index(request):
    if request.method == 'POST':
        del request.session['username']
        return render(request, 'index.html', {"username" : ""})
    else:
        if request.session.has_key('username'):
            username = request.session['username']
            return render(request,  'index.html', {"username" : username})
        else:
            return render(request, 'index.html', {"username" : ""})

def success(request):
    if request.session.has_key('username'):
        username = request.session['username']
    else:
        username=""
    return render(request,  'success.html', {"username" : ""})
    
def mistakes(request):
    if request.session.has_key('username'):
        username = request.session['username']
    else:
        username=""
    return render(request,  'mistakes.html', {"username" : ""})

def login(request):
    args = {}
    if request.method == 'POST':
        try:
            myusername = User.objects.filter(username=request.POST.get("user"))[0].username
        except:
            args = {}
            args['message'] = "Unknown Username!"
            return render(request, 'login.html',args)
        mypassword = User.objects.filter(username=request.POST.get("user"))[0].password
        if mypassword == request.POST.get("pass"):
            request.session['username'] = User.objects.filter(username=request.POST.get("user"))[0].username
            myusername = request.session['username']
            return render(request, 'success.html', {"username" : myusername})
        else:
            args = {}
            args['message'] = "Wrong Password!"
            return render(request, 'login.html',args)
    else:
        return render(request, 'login.html', {"username" : ""})