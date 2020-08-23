from django.db import models
from django.utils import timezone

# Create your models here.

# Master models

class Program(models.Model):
    name = models.CharField(max_length=64)
    discription = models.CharField(max_length=256)
    created_date = models.DateTimeField(default=timezone.now,editable=False)
    updated_date = models.DateTimeField(null=True,blank=True)

class Course(models.Model):
    name = models.CharField(max_length=64)
    discription = models.CharField(max_length=256)
    end = models.DateField(null=True,blank=True)
    created_date = models.DateTimeField(
            default=timezone.now,
            editable=False
            )
    updated_date = models.DateTimeField(
            null=True,blank=True)

    #FIXME 何Lessonあるか計上する関数

class Lesson(models.Model):
    name = models.CharField(max_length=64)
    code = models.IntegerField(default=0)
    discription = models.CharField(max_length=256)
    is_advanced = models.BooleanField(default=False)
    created_date = models.DateTimeField(
            default=timezone.now,
            editable=False
            )
    updated_date = models.DateTimeField(
            null=True,blank=True)
