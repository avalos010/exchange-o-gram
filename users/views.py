from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


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
        user = User.objects.get(username=request.user)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        location = request.POST['location']
        email = request.POST['email']

        if first_name and first_name != user.first_name:  # Dont Save if value didnt change!!
            user.first_name = first_name
            user.save()
        if last_name and last_name != user.last_name:  # Dont Save if value didnt change!!
            user.last_name = last_name
            user.save()
        if location and location != user.userprofile.location:  # Dont Save if value didnt change!!
            user.userprofile.location = location
            user.save()
        if email and email != user.email:  # Dont Save if value didnt change!!
            user.email = email
            user.save()

        return redirect('settings')
    else:
        return render(request, 'users/settings.html')


def change_password(request):

    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        old_password = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']

        form = PasswordChangeForm(data=request.POST, user=user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Changed!')
            return redirect('change_password')
        else:
            messages.error(request, form.errors)
            return render(request, 'users/change_password.html')
    return render(request, 'users/change_password.html')
