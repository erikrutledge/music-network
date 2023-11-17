from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
 
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
    bio = models.TextField()
    friends = models.ManyToManyField(User, related_name='+', blank=True)
    tracks = models.ManyToManyField(Track, blank=True)

    def __str__(self):
        return self.user.username

# Construct listeners to create and update a Profile extension on User creation
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()