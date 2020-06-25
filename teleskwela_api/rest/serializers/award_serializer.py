from rest_framework import serializers
from rest.models improt Award

class AwardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Award
        fields = ['name']
