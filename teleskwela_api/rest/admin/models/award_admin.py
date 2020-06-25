from django.contrib import admin

class AwardAdmin(admin.ModelAdmin):
    fields = ['name', 'toggled']
    
    