from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30)

class Category(models.Model):
    name = models.CharField(max_length=30)

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image_url =models.ImageField(upload_to='images/')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)