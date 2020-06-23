from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    awards = models.ManyToManyField(Award)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return first_name


class Award(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return name


class SubjectCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    subjectCategory = models.ForeignKey(SubjectCategory, on_delete = models.CASCADE)

    def __str__(self):
        return name


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)

    def __str__(self):
        return name


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE)

    def __str__(self):
        return name
