from rest_framework import viewsets
from rest.models import Award
from rest.serializers import AwardSerializer


class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
