# Python imports
import pytest
from datetime import timedelta

# Django imports
from django.utils import timezone

# Local imports
from rain.services import get_rian_by_fields
from field.models import Field
from rain.models import Rain


@pytest.mark.django_db
class TestFieldServices:

    def test_get_rian_by_fields_one(
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

        fields = get_rian_by_fields()

        assert len(fields) == 1

    def test_get_rian_by_fields_ok_two(
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

        Rain(
            field_owner=field,
            date=date,
            quantity=123
        ).save()

        fields = get_rian_by_fields()

        assert len(fields) == 1
