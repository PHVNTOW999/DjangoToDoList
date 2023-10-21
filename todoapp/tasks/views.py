from django.shortcuts import render

from .models import *


def index(req):
    tasks = Task.objects.all()
    return render(req, 'tasks/index.html', {'page_title': 'ToDo List', 'data': tasks})
