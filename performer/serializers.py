from rest_framework import serializers
from performer.models import Performer

class PerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = '__all__'