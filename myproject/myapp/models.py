from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(Teacher)
