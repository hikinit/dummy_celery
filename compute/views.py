from django.shortcuts import render
from django.http import HttpResponse
from compute.tasks import sleep as do_sleep
from compute.models import Task


def home(req):
    tasks = Task.objects.all()
    return HttpResponse("\n".join([f"{task.name} {task.status}" for task in tasks]))


def sleep(req, second=5):
    task = do_sleep.delay(second)
    return HttpResponse(f"{task.id} is sleeping for {second} seconds")