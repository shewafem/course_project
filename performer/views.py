from rest_framework.viewsets import ModelViewSet
from performer.serializers import PerformerSerializer
from performer.models import Performer



class PerformerViewSet(ModelViewSet):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer