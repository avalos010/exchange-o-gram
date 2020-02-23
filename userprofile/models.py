from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True, )
    photo = models.ImageField(upload_to=f"profile/")
    bio = models.TextField(blank=True, max_length=500)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    followers = models.ManyToManyField(
        'self', name="followers", symmetrical=False, blank=True, related_name='is_following_me')
    following = models.ManyToManyField(
        'self', name="following", symmetrical=False, blank=True, related_name='am_following')

    def get_birth_year(self):
        return datetime.now().year - self.date_of_birth.year

    def __str__(self):
        """Return human-readable representation"""
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
