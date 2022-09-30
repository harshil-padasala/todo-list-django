from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# task model
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task_title = models.CharField(max_length=200)
    description = models.TextField(null= True, blank=True)
    is_complete = models.BooleanField(default=False)
    created_time =  models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.task_title

    class Meta:
        ordering = ['is_complete']