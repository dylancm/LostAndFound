from django.db import models
from django.utils import timezone
import datetime


class Object(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=200)
    when = models.DateTimeField()

    def __unicode__(self):
        return self.title

    def recently_lost_found(self):
        return self.when >= timezone.now() - datetime.timedelta(days=3)
