from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
