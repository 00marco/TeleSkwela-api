from django.db import models
from rest.models.subject import Subject

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
