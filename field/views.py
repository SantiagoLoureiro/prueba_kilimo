# Python imports
import logging

# Django imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local imports
from field.models import Field
from field.serializers import FieldRainSerializer
from field.services import get_fields_by_rain_and_days


class FieldRainView(
        APIView
):
    queryset = Field.objects.all()
    serializer_class = FieldRainSerializer

    def get(self, request, *args, **kwargs):
        try:

            data = {}
            if "rain_quantity" in request.GET:
                data.update({
                    "rain_quantity": request.GET.get('rain_quantity'),
                })
            if "days_ago_rain" in request.GET:
                data.update({
                    "days_ago_rain": request.GET.get('days_ago_rain'),
                })

            rains = get_fields_by_rain_and_days(
                **data
            )

        except Exception as error_info:
            logging.exception(error_info)
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "error": error_info.args
                }
            )

        return Response(status=status.HTTP_200_OK, data=rains)
