from celery import shared_task
from compute.models import Task
import time


@shared_task(bind=True)
def sleep(self, x):
    task = Task.objects.create(name=self.request.id, status="PENDING")
    time.sleep(x)
    task.status = "FINISHED"
    task.save()
    return True
