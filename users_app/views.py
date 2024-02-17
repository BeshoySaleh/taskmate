from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method=="POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "New User Account Created, Login To Get Started!")
            return redirect('register')
    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})

def logout_user(request):
    logout(request)
    messages.success(request, "you have been logged out bye")
    return redirect('index')
