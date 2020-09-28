# Python imports
import pytest
from datetime import timedelta

# Django imports
from django.utils import timezone

# Local imports
from field.services import get_fields_by_rain_and_days
from field.models import Field
from rain.models import Rain


@pytest.mark.django_db
class TestFieldServices:

    def test_get_fields_by_rain_and_days_ok_one(
            self,
    ):

        field = Field(
            name="TEST"
        )
        field.save()

        date_delta = timedelta(
            days=4
        )
        date = timezone.now() - date_delta

        Rain(
            field_owner=field,
            date=date,
            quantity=123
        ).save()

        fields = get_fields_by_rain_and_days(
            days_ago_rain=7,
            rain_quantity=124
        )

        assert len(fields) == 0

    def test_get_fields_by_rain_and_days_ok_two(
            self,
    ):
        field = Field(
            name="TEST"
        )
        field.save()

        date_delta = timedelta(
            days=4
        )
        date = timezone.now() - date_delta

        Rain(
            field_owner=field,
            date=date,
            quantity=123
        ).save()

        fields = get_fields_by_rain_and_days(
            days_ago_rain=7,
            rain_quantity=122
        )

        assert len(fields) == 1

    def test_filter_fields_by_rain_days_ago_error(self):

        get_error = False
        try:
            get_fields_by_rain_and_days(
                days_ago_rain=8
            )
        except Exception:
            get_error = True

        assert get_error
