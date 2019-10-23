from django.db import models
from django.utils import timezone


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=225)
    number = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
