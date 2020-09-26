# Python imports
from typing import List
from datetime import timedelta

# Django imports
from django.utils import timezone
from django.db.models import QuerySet
from django.db.models import Avg


# Local imports
from field import selectors
from field import constants


def get_fields_whit_rain_prom(
        fields_qs: QuerySet = None
) -> List:

    if fields_qs is None:
        fields_qs = selectors.get_fields()

    data_respose = []

    for field in fields_qs:
        quantity_prom = field.rain.all().aggregate(Avg('quantity'))
        quantity__avg = quantity_prom['quantity__avg']
        data_respose.append(
            {
                "id": field.id,
                "name": field.name,
                "rain_quantity_average": quantity__avg
            }
        )

    return data_respose


def filter_fields_by_rain_days_age(
    fieds_qs: QuerySet = None,
    days_ago_rain: int = constants.MAX_DAYS_FOR_QUERY_FIELDS
):

    if days_ago_rain > constants.MAX_DAYS_FOR_QUERY_FIELDS:
        raise Exception("days_ago_rain should be < to "
                        f"{constants.MAX_DAYS_FOR_QUERY_FIELDS}")

    date_delta = timedelta(
        days=days_ago_rain
    )
    date_query = timezone.now() - date_delta

    fields_qs = selectors.get_fields_by_rain_date(
        date=date_query,
        fields_qs=fieds_qs
    )

    return fields_qs.distinct()


def get_fields_by_rain_and_days(
        rain_quantity: float = None,
        days_ago_rain: int = constants.MAX_DAYS_FOR_QUERY_FIELDS
):

    fields_qs = None
    if rain_quantity:
        fields_qs = selectors.get_fields_by_rain_quantity(
            quantity=rain_quantity,
            fields_qs=fields_qs
        )

    if days_ago_rain:
        fields_qs = filter_fields_by_rain_days_age(
            fieds_qs=fields_qs
        )

    response_data = get_fields_whit_rain_prom(
        fields_qs=fields_qs
    )

    return response_data
