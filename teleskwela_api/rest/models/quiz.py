from django.db import models
from rest.models.lesson import Lesson

class Quiz(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    total_number_of_items = models.IntegerField(required=True)

    lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE)


    def __str__(self):
        return self.name
