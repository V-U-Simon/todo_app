from tabnanny import verbose
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    date_create = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        ordering = ('date_create',)
