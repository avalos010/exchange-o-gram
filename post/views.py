from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from userprofile.models import UserProfile
from .models import Post

# Create your views here.


def feed(request):
    if request.user.is_authenticated:
        posts = Post.objects.order_by('-date')

        return render(request, 'posts/feed.html', {'posts': posts})
    else:
        messages.error(request, 'Must be logged in to view your feed!')
        return redirect('login')
