from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from userprofile.models import UserProfile
from .models import Post, Comment
from django.db.models import Q
import json

# Create your views here.


def feed(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(
            Q(profile__followers=request.user.userprofile.id) | Q(profile_id=request.user.userprofile.id)).order_by('-date')
        comments = Comment.objects.all().order_by('-date')

        return render(request, 'posts/feed.html', {'posts': posts, 'comments': comments})
    else:
        messages.error(request, 'Must be logged in to view your feed!')
        return redirect('login')


def like_post(request):
    if request.method == 'POST':
        json_id = json.loads(request.body)['id']
        post = Post.objects.get(id=json_id)
        post.likes.add(request.user.userprofile.id)
        return redirect('feed')


def unlike_post(request):
    if request.method == 'POST':
        json_id = json.loads(request.body)['id']
        post = Post.objects.get(id=json_id)
        post.likes.remove(request.user.userprofile.id)
        return redirect('feed')
