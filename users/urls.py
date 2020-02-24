
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('settings', views.settings, name='settings'),
    path('logout', views.logout, name='logout'),
    path('change_password', views.change_password, name="change_password")

]
