# Django imports
from django.db.models import QuerySet

# Local imports
from field import selectors
from rain.models import Rain


def get_rains_order_by_fields(
        fields_qs: QuerySet = None
) -> QuerySet:

    if fields_qs is None:
        fields_qs = selectors.get_fields()

    rains = Rain.objects.filter(field_owner__in=fields_qs).order_by(
        'field_owner'
    )

    return rains
