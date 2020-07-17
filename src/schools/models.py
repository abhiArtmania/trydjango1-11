from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    # Change the objectname with name of school (in django admin)
    def __str__(self):
        return self.name
