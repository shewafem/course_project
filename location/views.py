from rest_framework.viewsets import ModelViewSet
from location.serializers import LocationSerializer
from location.models import Location



class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer