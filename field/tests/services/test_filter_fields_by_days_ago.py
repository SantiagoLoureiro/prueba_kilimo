# Python imports
import pytest
from datetime import timedelta

# Django imports
from django.utils import timezone

# Local imports
from field.services import filter_fields_by_rain_days_ago
from field.models import Field
from rain.models import Rain


@pytest.mark.django_db
class TestFieldServices:

    def test_filter_fields_by_rain_days_ago_ok_one(
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

        fields = filter_fields_by_rain_days_ago(
            days_ago_rain=7
        )

        assert len(fields) == 1

    def test_filter_fields_by_rain_days_ago_ok_two(
            self,
    ):

        field = Field(
            name="TEST"
        )
        field.save()

        date_delta = timedelta(
            days=10
        )
        date = timezone.now() - date_delta

        Rain(
            field_owner=field,
            date=date,
            quantity=123
        ).save()

        fields = filter_fields_by_rain_days_ago(
            days_ago_rain=7
        )

        assert len(fields) == 0

    def test_filter_fields_by_rain_days_ago_error(self):

        get_error = False
        try:
            self.service(
                days_ago_rain=8
            )
        except:
            get_error = True

        assert get_error

