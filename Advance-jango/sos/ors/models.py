from modulefinder import Module

from django.db import models

# Create your models here.
class User(models.Model):
     firstName = models.CharField(max_length=100)
     lastName = models.CharField(max_length=100)
     loginId = models.CharField(max_length=100)
     password = models.CharField(max_length=100)
     dob = models.DateField()
     address = models.CharField(max_length=100)
     class Meta:
         db_table = "sos_user"
