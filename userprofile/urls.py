
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.profile, name='profile'),
    path('follow', views.follow, name='follow'),
    path('unfollow', views.unfollow, name='unfollow')

]
