from django.db import models
from django.contrib.auth.models import User

 
class Track(models.Model):
    username = models.ManyToManyField(User)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    img = models.URLField(max_length=200)

    def __str__(self):
        return self.title

# Extend the User Model by creating a one-to-one link with a Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default="./static/images/default.jpeg", upload_to='./static/images')
    bio = models.TextField()
    friends = models.ManyToManyField(User, related_name='+')
    tracks = models.ManyToManyField(Track)

    def __str__(self):
        return self.user.username