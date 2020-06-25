from django.db import models
from rest.models.student import Student
from rest.models.subjectCategory import SubjectCategory

class Subject(models.Model):
    name = models.CharField(max_length=100)
    student = models.ManyToManyField(Student)
    subjectCategory = models.ForeignKey(SubjectCategory, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
