# Python imports
import logging

# Django imports
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

# Local imports
from rain.models import Rain
from rain.serializers import RainSerializer
from rain.services import get_rian_by_fields


class RainView(
        mixins.CreateModelMixin,
        GenericAPIView
):
    queryset = Rain.objects.all()
    serializer_class = RainSerializer

    def get(self, request, *args, **kwargs):
        try:
            rains = get_rian_by_fields()
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