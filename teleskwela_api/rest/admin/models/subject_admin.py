from django.contrib import admin

class SubjectAdmin(admin.ModelAdmin):
    fields = ['name']
