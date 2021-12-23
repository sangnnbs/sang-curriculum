from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    slug = models.SlugField(max_length=150)
    image = models.ImageField(upload_to="images/", default="images/default.png")

    def __str__(self) -> str:
        return self.title