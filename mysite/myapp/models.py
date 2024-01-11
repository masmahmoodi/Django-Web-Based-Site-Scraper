from django.db import models

# Create your models here.

class Data(models.Model):
    link = models.TextField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
