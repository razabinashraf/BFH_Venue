from django.db import models
from django.db.models.base import Model

# Create your models here.
class event(models.Model) :
    title = models.CharField(max_length=30)
    datetime = models.DateTimeField()
    location = models.CharField(max_length=30)
    max_participants = models.IntegerField()
    description = models.TextField()
