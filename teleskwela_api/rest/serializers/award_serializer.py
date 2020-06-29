from rest_framework import serializers
from rest.models import Award

class AwardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Award
        fields = ['name']
