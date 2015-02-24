# coding: utf-8

from django.contrib import admin
from training.models import Task

class TaskionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('content', 'created', 'was_published_recently')