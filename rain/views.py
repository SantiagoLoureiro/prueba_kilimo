# Django imports
from rest_framework import mixins
from rest_framework.generics import GenericAPIView

# Local imports
from rain.models import Rain
from rain.serializers import RainSerializer


class RainView(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        GenericAPIView
):
    queryset = Rain.objects.all()
    serializer_class = RainSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = self.create(request, *args, **kwargs)
        print(data)
        return data