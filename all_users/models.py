from django.db import models


# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    u_image = models.ImageField(upload_to='news/images/')

    def __str__(self):
        return self.username
