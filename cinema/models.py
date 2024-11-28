from django.db import models
from django.db.models import Q

class Movie(models.Model):
    movie_title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    screening_date = models.DateField()
    screening_time = models.TimeField()
    theater_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    ticket_price = models.DecimalField(max_digits=5, decimal_places=5)
    available_seats = models.PositiveIntegerField()
