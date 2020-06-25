from rest_framework import viewsets
from rest.models import Lesson  
from rest.serializers import LessonSerializer 

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
