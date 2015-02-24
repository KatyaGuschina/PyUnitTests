from django.shortcuts import render_to_response
from django.template import RequestContext
from training.models import Task
from django.views.generic import ListView, DetailView


class TaskListView(ListView):
    model = Task


class TaskDetailView(DetailView):
    model = Task


def index(request):
    return render_to_response('training/task_list.html', context_instance=RequestContext(request))