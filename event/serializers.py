from xml.dom.minidom import AttributeList
from rest_framework import serializers
from event.models import Event
from performer.models import Performer
from location.models import Location

class PerformerSerializerForEvent(serializers.ModelSerializer):
    class Meta:
        model = Performer
        #fields = "__all__"
        fields = ['name']

class LocationSerializerForEvent(serializers.ModelSerializer):
    class Meta:
        model = Location
        #fields = "__all__"
        fields = ['name']


class EventSerializer(serializers.ModelSerializer):
    performer_data = PerformerSerializerForEvent(source='performer', many=True)
    location_data = LocationSerializerForEvent(source='location', many=True)
    class Meta:
        model = Event
        #fields = '__all__'
        exclude = ['performer']
        exclude = ['location']