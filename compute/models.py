from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200, unique=True)
    status = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
