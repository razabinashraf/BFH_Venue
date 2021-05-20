from django.db import models

# Create your models here.
class User(models.Model) :
    name = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=10)
    place = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)

