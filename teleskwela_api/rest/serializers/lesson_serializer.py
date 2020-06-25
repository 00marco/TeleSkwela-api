from rest_framework import serializers
from rest.models import Lesson

class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name']
