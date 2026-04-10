from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='task_images/', null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title