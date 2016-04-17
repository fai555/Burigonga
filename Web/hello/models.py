from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField()

class WaterParticle(models.Model):    
    deviceID = models.CharField(max_length=50)   
    user = models.CharField(max_length=50,null = True)
    ph = models.FloatField(blank=True,null = True)
    temperature = models.FloatField(blank=True,null = True)
    orp = models.FloatField(blank=True,null = True)
    dateTime = models.DateTimeField(blank=True,null = True)
    geoLocation = models.CharField(max_length=254,blank=True,null = True)
    def __unicode__(self):
        return self.deviceID


class UserDevice(models.Model):
    user = models.CharField(max_length=50)
    deviceID = models.CharField(max_length=50)
    def __unicode__(self):
        return self.deviceID

