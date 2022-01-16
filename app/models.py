from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_GROUP = (
    ('All', 'All'),
    ('Kids', 'Kids'),
    ('Adults', 'Adults')
)

MOVIE_CHOICES = (
    ('Seasonal', 'Seasonal'),
    ('Single', 'Single')
)


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', blank=True)


class Profile(models.Model):
    name = models.CharField(max_length=255)
    age_limit = models.CharField(max_length=10, choices=AGE_GROUP)
    uuid = models.UUIDField(default=uuid.uuid4)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    videos = models.ManyToManyField('Video')
    thumbnail = models.ImageField(upload_to='thumbnails')
    age_limit = models.CharField(max_length=10, choices=AGE_GROUP)


class Video(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to='movie')
