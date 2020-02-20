from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
import json
from django.core.exceptions import ObjectDoesNotExist
from post.models import Post
# Create your views here.


def profile(request, username):
    try:
        profile = get_object_or_404(UserProfile, user__username=username)
        # following = UserProfile.objects.filter(followers=profile.id)
        # print('current profile:', profile)
        # print(f'loggedin user: {request.user.userprofile.id}')
        is_following = bool(profile.followers.filter(
            id=request.user.userprofile.id))
        # print(f'is following: {is_following}')
        # print(f'following_profiles: {following}')
        # print(f"current_followers:{profile.followers.all()}")
        # posts = Post.objects.filter(profile=profile)
        # print(profile.post)
        posts = Post.objects.filter(profile_id=profile.id)
        context = {
            'profile': profile,
            'following': is_following,
            'posts': posts
        }
        return render(request, 'profile/profile.html', context)
    except AttributeError:
        profile = get_object_or_404(UserProfile, user__username=username)

        return render(request, 'profile/profile.html', {'profile': profile})


def follow(request):
    if request.method == 'POST':

        userid = request.POST['userid']
        username = request.POST['username']
        profile = get_object_or_404(UserProfile, user__username=username)

        if userid != request.user.userprofile.id and username != request.user.userprofile:

            profile.followers.add(request.user.userprofile.id)
            request.user.userprofile.following.add(profile.id)
            print('followers', request.user.userprofile.followers.all())
            return redirect('profile', username)


def unfollow(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        username = request.POST['username']
        profile = get_object_or_404(UserProfile, user__username=username)
        profile.followers.remove(request.user.userprofile.id)
        request.user.userprofile.following.remove(profile.id)

        return redirect('profile', username)


def edit_user(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        location = request.POST['location']
        # picture = request.POST['profile_pic']

        if first_name:
            user.first_name = first_name
            user.save()
        if last_name:
            user.last_name = last_name
            user.save()
        if location:
            user.userprofile.location = location
            user.save()
        # if picture is not None:
        #     user.userprofile.photo = picture
        #     user.save()
        return profile(request, user)
