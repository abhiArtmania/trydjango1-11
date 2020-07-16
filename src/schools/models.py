from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
