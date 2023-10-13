from django.db import models

class User(models.Model):
    username = models.CharField(max_length=16)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    img = models.ImageField(default='static/images/default.jpeg', upload_to='static/images/')
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.username}"

class Track(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #?
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    img = models.ImageField()

