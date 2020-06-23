from django.contrib import admin
from .models import User, Award, Lesson, Quiz, Subject, SubjectCategory
# Register your models here.

admin.site.register(User)
admin.site.register(Award)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Subject)
admin.site.register(SubjectCategory)
