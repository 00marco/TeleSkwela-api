from rest_framework import viewsets
from rest.models import Quiz  
from rest.serializers import QuizSerializer  


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer