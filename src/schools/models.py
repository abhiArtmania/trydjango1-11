from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from .validators import validate_name, validate_location
from django.conf import settings
from django.urls import reverse

User = settings.AUTH_USER_MODEL

class SchoolQuerySet(models.query.QuerySet):
    def search(self,query):
        if query:
            query = query.strip()
            Q = models.Q
            return self.filter(
                Q(name__icontains=query) | Q(location__icontains=query) | Q(item__name__icontains=query) | Q(item__contents__icontains=query)
            ).distinct()
        else:
            return self

class SchoolManager(models.Manager):
    def get_queryset(self):
        return SchoolQuerySet(self.model, using=self._db)

    def search(self,query):
        return self.get_queryset().search(query)

class School(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, validators=[validate_name])
    location = models.CharField(max_length=120, null=True, blank=True, validators=[validate_location])
    timestamp = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True,blank=True)

    objects = SchoolManager()

    # Change the objectname with name of school (in django admin)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('schools:detail', kwargs={'slug':self.slug})

    # title = name
    def title(self):
        return self.name

def school_pre_save_receiver(sender, instance, *args, **kwargs):
     instance.location = instance.location.capitalize()
     if not instance.slug:
         instance.slug = unique_slug_generator(instance)

##### we can't save slug in post_save. It will goes under infinite loop. that's why I'm commenting this.
# def school_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('Saved')
#     print(instance.timestamp)
#     print(created)

pre_save.connect(school_pre_save_receiver, sender=School)
# post_save.connect(school_post_save_receiver, sender=School)
