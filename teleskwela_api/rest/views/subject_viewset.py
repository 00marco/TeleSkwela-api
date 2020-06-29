from rest_framework import viewsets
from rest.models import Subject 
from rest.serializers import SubjectSerializer 


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
