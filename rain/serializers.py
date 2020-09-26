# Django imports
from rest_framework import serializers

# Local imports
from rain.models import Rain


class RainSerializer(serializers.ModelSerializer):
    field_id = serializers.CharField()

    class Meta:
        model = Rain
        fields = ['date', 'quantity']
