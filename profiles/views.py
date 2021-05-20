from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def home(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password= password)

        if user is not None :
            auth.login(request, user)
            return redirect("events/view")
        else :
            messages.info(request, 'Invalid credentials')
            return redirect('/')
    else :
        return render(request, 'index.html')
def register(request) :
    return render(request, 'register.html')