from rest_framework import serializers
from rest.models import Subject

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ['name']


