# Django imports
from rest_framework import serializers

# Local imports
from rain.models import Rain


class RainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rain
        fields = ['date', 'quantity', 'field_owner']
