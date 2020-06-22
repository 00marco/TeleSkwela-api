from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)

class Award(models.Model):
    name = models.CharField(max_length=100)

class SubjectCategory(models.Model):
    name = models.CharField(max_length=100)

class Subject(models.Model):
    name = models.CharField(max_length=100)

class Lesson(models.Model):
    name = models.CharField(max_length=100)

class Quiz(models.Model):
    name = models.CharField(max_length=100)

