# Python imports
import logging

# Django imports
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

# Local imports
from field.models import Field
from field.serializers import FieldRainSerializer
from field.services import get_fields_by_rain_and_days


class FieldRainView(
        mixins.CreateModelMixin,
        GenericAPIView
):
    queryset = Field.objects.all()
    serializer_class = FieldRainSerializer

    def get(self, request, *args, **kwargs):
        try:
            rains = get_fields_by_rain_and_days(
                **request.data
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

    def post(self, request, *args, **kwargs):
        data = self.create(request, *args, **kwargs)
        return data