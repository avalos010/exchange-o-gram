from django.db import models
from userprofile.models import UserProfile
from datetime import datetime

# Create your models here.


class Post(models.Model):
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="media")
    profile = models.ForeignKey(
        UserProfile, on_delete=models.DO_NOTHING, default=None)
    date = models.DateTimeField(default=datetime.now, blank=True)
    likes = models.ManyToManyField(
        UserProfile, related_name='likes', blank=True)

    def __str__(self):
        return self.body[:10]


class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(UserProfile,  on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.body[:10]
