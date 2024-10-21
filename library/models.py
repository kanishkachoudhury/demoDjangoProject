from django.utils import timezone
from django.db import models
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_date = models.DateField(default=timezone.now)
    author = models.ManyToManyField(Author,related_name='books')

class Location(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    enroll_date = models.DateField(auto_now=True)

class BooksTaken(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date_taken = models.DateField(auto_now=True)