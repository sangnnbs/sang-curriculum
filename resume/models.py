from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=30, default='Sang')
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    github = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    avatar = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    project_link1 = models.CharField(max_length=100, blank=True)
    project_link2 = models.CharField(max_length=100, blank=True)
    project1 = models.TextField(null=True)
    project2 = models.TextField(null=True)
    
