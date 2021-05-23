from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.
class event(models.Model) :
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    datetime = models.DateTimeField()
    location = models.CharField(max_length=30)
    max_participants = models.IntegerField()
    description = models.TextField()

class register_event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(event, on_delete= models.CASCADE)

