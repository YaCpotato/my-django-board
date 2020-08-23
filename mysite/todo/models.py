from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=64)
    start = models.DateField(default=timezone.now)
    end = models.DateField(null=True,blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            null=True,blank=True)
    finished_date = models.DateTimeField(
            null=True,blank=True)