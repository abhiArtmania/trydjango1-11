from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True,blank=True)

    # Change the objectname with name of school (in django admin)
    def __str__(self):
        return self.name

    # title = name
    def title(self):
        return self.name

def school_pre_save_receiver(sender, instance, *args, **kwargs):
     print('Saving...')
     print(instance.timestamp)
     if not instance.slug:
         instance.slug = unique_slug_generator(instance)
         instance.save()

##### we can't save slug in post_save. It will goes under infinite loop. that's why I'm commenting this.
# def school_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('Saved')
#     print(instance.timestamp)
#     print(created)

pre_save.connect(school_pre_save_receiver, sender=School)
post_save.connect(school_post_save_receiver, sender=School)
