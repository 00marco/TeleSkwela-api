from django.db import models
from rest.models.student import Student 

class Award(models.Model):
    name = models.CharField(max_length=100)
    student = models.ManyToManyField(Student)
    toggled = models.BooleanField(default=False)
    def __str__(self):
        return self.name 
