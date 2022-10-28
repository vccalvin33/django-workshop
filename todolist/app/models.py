from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=150)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    task_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_owner + ": " + self.task