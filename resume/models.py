from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    github = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    avatar = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    
