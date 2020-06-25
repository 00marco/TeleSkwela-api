from django.contrib import admin
from rest.models import *
from rest.admin.models import *


admin.site.header = "Teleskwela API"
admin.site.register(Student, StudentAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectCategory, SubjectCategoryAdmin)
