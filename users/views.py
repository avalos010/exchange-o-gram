from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('feed')
            else:
                messages.error(request, 'Invalid Login Info')
                return redirect('login')
        else:  # form is not valid
            messages.error(request, 'Invalid Login Info')
            return redirect('login')
    else:
        return render(request, 'users/login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Succesfully registered! You may now login.')
            return redirect('login')
        else:
            messages.error(request, form.errors)
            return redirect('register')
    else:
        return render(request, 'users/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


def settings(request):
    if request.method == 'POST':
        return
    else:
        return render(request, 'users/settings.html')
