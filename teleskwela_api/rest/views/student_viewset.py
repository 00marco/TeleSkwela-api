from rest_framework import viewsets
from rest.models import Student 
from rest.serializers import StudentSerializer 


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().orderby()
    serializer_class = StudentSerializer
