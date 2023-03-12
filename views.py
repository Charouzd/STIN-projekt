from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import views
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,"index.html")
def log_in(request):
    if request.method =="POST":
        #request.POST['id'] - also possible
        accouunt_number = request.POST.get('username')
        accouunt_password = request.POST.get('password')
        my_user = authenticate(username=accouunt_number)
        if my_user is not None:
            login(request,accouunt_number)
            return render(request,"index.html",{"name":my_user.name})
        else:
            messages.error(request,"wrong number or password")
        
    return render(request,"loggin.html")
def register(request):
    if request.method =="POST":
        #request.POST['id'] - also possible
        accouunt_number = request.POST.get('username')
        accouunt_password = request.POST.get('password')
        accouunt_mail = request.POST.get('mail')
        accouunt_name = request.POST.get('name')
        my_user= User.objects.create_user(accouunt_number,accouunt_password,accouunt_mail)
        my_user.name=accouunt_name
        my_user.save()
        messages.success(request,"You have succeessfuly logged in succeessfully")
        return redirect('log_in')
    return render(request,"register.html")