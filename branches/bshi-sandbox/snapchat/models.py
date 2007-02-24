from django.db import models

from django.contrib.auth.models import User 

# Create your models here.


MAX_NAME_LENGTH = 32

class Channel(models.Model):
    name = models.CharField(maxlength=16) 
    description = models.TextField()
    private = models.BooleanField(default=False)    # only allow Users

    class Admin:
        pass

class Chatter(models.Model):
    name = models.CharField(maxlength=16)
    ip = models.IPAddressField()
    channel = models.ForeignKey(Channel)

class Statement(models.Model): 
    name = models.CharField(maxlength=MAX_NAME_LENGTH) 
    text = models.TextField() 
    date = models.DateTimeField(auto_now_add=True)
    channel = models.ForeignKey(Channel)
