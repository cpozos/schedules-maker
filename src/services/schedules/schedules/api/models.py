from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Degree(models.Model):
    name = models.CharField(max_length=200, unique=True)
    num_periods = models.PositiveIntegerField()
    subjects = models.ManyToManyField(Subject, through='DegreeSubject')

class DegreeSubject(models.Model):
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    period = models.PositiveIntegerField() #desired

class Semester(models.Model):
    name = models.CharField(max_length=6, unique=True)
    open_subjects = models.ManyToManyField(Subject)