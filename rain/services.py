# Django imports
from django.db.models import QuerySet

# Local imports
from rain import selectors as rain_selectors
from rain.serializers import RainSerializer

from field import selectors as filed_selectors


def get_rian_by_fields(
        fields_qs: QuerySet = None
):

    if fields_qs is None:
        fields_qs = filed_selectors.get_fields()

    rain_qs = rain_selectors.get_rains_order_by_fields(
        fields_qs=fields_qs
    )

    data_return = []

    for field in fields_qs:
        rains = rain_qs.filter(field_owner=field)
        serializer = RainSerializer(data=list(rains), many=True)
        serializer.is_valid()
        data_return.append(serializer.data)

    return data_return

