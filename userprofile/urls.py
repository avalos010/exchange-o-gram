
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.profile, name='profile'),
    path('follow', views.follow, name='follow'),
    path('unfollow', views.unfollow, name='unfollow'),
    path('edit_user', views.edit_user, name="edit_user"),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('add_comment', views.add_comment, name="add_comment")

]
