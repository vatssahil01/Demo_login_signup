from django.shortcuts import render,redirect
from django.http import HttpResponse
from Demoapp.models import *

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = login.objects.get(username=username, password=password)
            return redirect('/msd/')
        except:
            return render(request,'login_2.html')
    return render(request, 'login.html')

def sign(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        signup = Signup(username=username, email=email, password=password)
        signup.save()
        return redirect('/login/')


    return render(request,'sign.html')

def login2(request):
    return render(request,'login_2.html')