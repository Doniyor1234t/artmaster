from django.db import models

# Create your models here.


class Arts(models.Model):
    name = models.CharField(max_length=500)
    number = models.CharField(max_length=500)
    size = models.CharField(max_length=500)
    type = models.CharField(max_length=500)
    data = models.DateTimeField(auto_now_add=True) 
    imageUrl = models.TextField()

class Frames(models.Model):
    shifr = models.CharField(max_length=500)
    number = models.CharField(max_length=500)
    bold = models.CharField(max_length=500)
    type = models.CharField(max_length=500)
    data = models.DateTimeField(auto_now_add=True) 
    imageUrl = models.TextField()

# class Thing(models.Model):
#     name = models.CharField(max_length=500)
#     number = models.CharField(max_length=500)
#     size = models.CharField(max_length=500)
#     type = models.CharField(max_length=500)
#     data = models.DateTimeField(auto_now_add=True) 
#     imageUrl = models.TextField()