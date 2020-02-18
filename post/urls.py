from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.feed, name="feed"),
    path('like_post', views.like_post, name="like_post"),
    path('unlike_post', views.unlike_post, name="unlike_post")

]
