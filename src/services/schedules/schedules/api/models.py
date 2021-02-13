from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Degree(models.Model):
    name = models.CharField(max_length=200, unique=True)
    num_periods = models.PositiveIntegerField()
    subjects = models.ManyToManyField(Subject, through='DegreeSubject')

class DegreeSubject(models.Model):
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    period = models.PositiveIntegerField() #desired

class Professor(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    is_assistant = models.BooleanField(default=False)

class SubjectOption(models.Model):
    SEMESTERS = [
        (1,'2021-2'), 
        (2,'2022-1'), 
        (3,'2022-2'),
        (4,'2023-1'), 
        (5,'2023-2'),
        (6,'2024-1'), 
        (7,'2024-2'),
        (8,'2025-1'), 
        (9,'2025-2'),
        (10,'2026-1'), 
        (11,'2026-2'),
        (12,'2027-1'), 
        (13,'2027-2'),
        (14,'2028-1'), 
        (15,'2028-2'),
        (16,'2029-1'), 
        (17,'2029-2')]

    semester = models.CharField(max_length=6, choices=SEMESTERS)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)

class Lesson(models.Model):
    DAYS = [
        (1,'Lunes'),
        (2,'Martes'),
        (3,'Miercoles'),
        (4,'Jueves'),
        (5,'Viernes'),
        (6,'Sabado'),
        (7,'Domingo')]

    subject_option = models.ForeignKey(SubjectOption, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    day = models.CharField(max_length=20, choices=DAYS)
    time_ini = models.TimeField(null=False, blank=False)
    time_end = models.TimeField(null=False, blank=False)