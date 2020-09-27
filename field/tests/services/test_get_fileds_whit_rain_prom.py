# Python imports
import pytest
from datetime import timedelta

# Django imports
from django.utils import timezone

# Local imports
from field.services import get_fields_whit_rain_prom
from field.models import Field
from rain.models import Rain


@pytest.mark.django_db
class TestFieldServices:

    def test_get_fields_whit_rain_prom_ok_one(
            self,
    ):

        field = Field(
            name="TEST"
        )
        field.save()

        date = timezone.now()

        Rain(
            field_owner=field,
            date=date,
            quantity=100
        ).save()

        Rain(
            field_owner=field,
            date=date,
            quantity=200
        ).save()

        fields = get_fields_whit_rain_prom()

        assert fields[0]['rain_quantity_average'] == 150.0
        assert len(fields) == 1


