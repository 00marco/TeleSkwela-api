from rest_framework import viewsets
from rest.models import SubjectCategory  
from rest.serializers import SubjectCategorySerializer 


class SubjectCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubjectCategory.objects.all()
    serializer_class = SubjectCategory
