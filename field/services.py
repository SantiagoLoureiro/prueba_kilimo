# Python imports
from datetime import timedelta

# Django imports
from django.utils import timezone
from django.db.models import QuerySet

# Local imports
from field import selectors
from field import constants


def get_fields_whit_rain_prom(
        fields_qs: QuerySet = None
) -> QuerySet:

    if fields_qs is None:
        fields_qs = selectors.get_fields()

    data_respose = []

    for field in fields_qs:
        rains = field.rain
        print(rains)



def get_fields_by_rain_and_days(
        rain_quantity: float = None,
        days_ago_rain: int = constants.MAX_DAYS_FOR_QUERY_FIELDS
):

    if not rain_quantity and not days_ago_rain:
        raise Exception("rain_qantity or days_ago_rain should be set")

    fields_qs = QuerySet()

    if rain_quantity:
        fields_qs = selectors.get_fields_by_rain_quantity(
            quantity=rain_quantity
        )

    if days_ago_rain:
        if days_ago_rain > constants.MAX_DAYS_FOR_QUERY_FIELDS:
            raise Exception("days_ago_rain should be < to "
                            f"{constants.MAX_DAYS_FOR_QUERY_FIELDS}")

        date_delta = timedelta(
            days=days_ago_rain
        )

        date_query = timezone.now() - date_delta

        fields_qs = selectors.get_fields_by_rain_date(
            date=date_query
        )

    response_data = get_fields_whit_rain_prom(
        fields_qs=fields_qs
    )

    return response_data
