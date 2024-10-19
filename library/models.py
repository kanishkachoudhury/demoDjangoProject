from django.utils import timezone
from django.db import models
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_date = models.DateField(default=timezone.now)

class Location(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)