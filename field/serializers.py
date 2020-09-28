# Django imports
from rest_framework import serializers

# Local imports
from field.models import Field


class FieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Field
        fields = ['name']


class FieldRainSerializer(serializers.Serializer):
    rain_quantity = serializers.FloatField(required=False)
    days_ago_rain = serializers.IntegerField(required=False)
