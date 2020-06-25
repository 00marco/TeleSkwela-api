from rest_framework import serializers
from rest.models import Quiz

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ['name']
