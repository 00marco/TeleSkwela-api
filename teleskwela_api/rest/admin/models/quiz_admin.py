from django.contrib import admin

class QuizAdmin(admin.ModelAdmin):
    fields = ['name']
