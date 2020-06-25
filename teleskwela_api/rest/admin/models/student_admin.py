from django.contrib import admin
from django import forms
from rest.models.award import Award
import django.dispatch

class TestModelForm(forms.ModelForm):
    toggleAllAwardsField = forms.BooleanField(required=False)#set initial = false or empty value will result to not defined erropr

    def save(self, commit = True):
        #  HOW TO SET AWARDS? USE A SIGNAL?

        # form_saved_signal = django.dispatch.Signal(providing_args=["toggleAllAwardsField"])
        # form_saved_signal.send(sender=self.__class__, toggleAllAwardsField=toggleAllAwardsField)
        
        return super(TestModelForm, self).save(commit = commit) #TODO unsa nang commit


class StudentAdmin(admin.ModelAdmin):
    form = TestModelForm
    fieldsets = (
        (None, {
            'fields': ('first_name', 'toggleAllAwardsField'),
        }),
    )

    def updateAllAwards(self, value):
        awards = Award.objects.all().update(toggled = value)

    def save_model(self, request, obj, form, change):
        # print("obj - {}".format(obj.__dict__))
        # print("form - {}".format(form.cleaned_data['toggleAllAwardsField']))
        # print("request - {}".format(request.__dict__))
        self.updateAllAwards(form.cleaned_data['toggleAllAwardsField'])
        super().save_model(request, obj, form, change)

    