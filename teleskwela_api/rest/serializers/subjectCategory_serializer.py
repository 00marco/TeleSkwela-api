from rest_framework import serializers
from rest.models import SubjectCategory

class SubjectCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubjectCategory
        fields = ['name']