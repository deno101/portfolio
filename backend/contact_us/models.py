from django.db import models
import datetime


# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)
    date = models.DateTimeField(default=datetime.datetime.now,)
