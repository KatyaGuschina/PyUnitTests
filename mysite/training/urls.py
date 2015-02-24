# coding: utf-8
from django.conf.urls import patterns, url

from training.views import TaskDetailView, TaskListView

urlpatterns = patterns('',
    url(r'^$', TaskListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', TaskDetailView.as_view()),
)