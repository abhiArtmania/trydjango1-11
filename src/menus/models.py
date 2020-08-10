from django.conf import settings
from django.db import models
from schools.models import School
from django.core.urlresolvers import reverse

class Item(models.Model):
    # associations
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    school      = models.ForeignKey(School)
    # item stuff
    name        = models.CharField(max_length=120)
    contents    = models.TextField(help_text='Separate each item by comma')
    excludes    = models.TextField(blank=True, null=True, help_text='Separate each item by comma')
    public      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updatedAt   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updatedAt','-timestamp'] # Item.objects.all()

    def get_absolute_url(self):
        return reverse('menus:detail', kwargs={'pk':self.pk})

    def get_contents(self):
        return self.contents.split(',')

    def get_excludes(self):
        return self.excludes.split(',')
