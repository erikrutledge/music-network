from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Track(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #?
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    img = models.URLField(max_length=200)

