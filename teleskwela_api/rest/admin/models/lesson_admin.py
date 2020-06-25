from django.contrib import admin

class LessonAdmin(admin.ModelAdmin):
    fields = ['name']
