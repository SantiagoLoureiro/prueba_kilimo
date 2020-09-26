# Python imports
from datetime import datetime, date

# Django imports
from django.db.models import QuerySet

# Local imports
from field.models import Field


def get_fields():

    return Field.objects.all()


def get_fields_by_rain_quantity(
        quantity: float,
        fields_qs: QuerySet = None
) -> QuerySet:

    if fields_qs is None:
        fields_qs = get_fields()

    return fields_qs.filter(
        quantity__gte=quantity
    )


def get_fields_by_rain_date(
        date: date,
        fields_qs: QuerySet = None
) -> QuerySet:

    if fields_qs is None:
        fields_qs = get_fields()

    return fields_qs.filter(
        rain__date__gte=date
    )