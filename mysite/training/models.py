#coding: utf-8
import datetime

from django.db import models
from django.utils import timezone


class Task(models.Model):
    created = models.DateTimeField(u'Дата создания')
    content = models.TextField(max_length=10000, blank=True)
    result = models.TextField(max_length=10000, blank=True)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created <= now

    def __unicode__(self):
        return self.content

    def get_absolute_url(self):
        return "/training/%i/" % self.id


