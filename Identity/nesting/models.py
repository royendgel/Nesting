from django.db import models
from django.contrib.auth.models import User
from Identity import settings
import datetime


# Create your models here.

class Identity_unique(models.Model):

    NIS = models.CharField(max_length = 200, primary_key = True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    Timestamp = models.DateTimeField(auto_now = True)

    First_Name = models.CharField(max_length = 80, null = True,  )

    Last_Name = models.CharField(max_length = 80, null = True, )

    location = models.CharField(max_length = 100, blank = True)

    date_of_birth = models.DateField(auto_now = False, auto_now_add = False)

    Contact = models.CharField(max_length = 15, null = True)



class Symptoms(models.Model):

    Symptoms_description = models.TextField(max_length = 900, null = True)
    Unique_Identities = models.ManyToManyField(Identity_unique)


class Treatment(models.Model):

    last_Treatment = models.TextField()
