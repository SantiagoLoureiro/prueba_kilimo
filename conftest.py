# Python imports
import pytest
from model_bakery import baker

# Django imports
from django.utils import timezone

# Local imports
from field import models as field_models
from rain import models as rain_models


@pytest.fixture
def data_db():
    field = baker.make(
        rain_models.Field,
        name="TEST_FIELD_NAME"
    )

    baker.make(
        field_models.Hectare,
        field_owner=field
    )
    baker.make(
        field_models.Hectare,
        field_owner=field
    )

    test_rain_one = baker.make(
        rain_models.Rain,
        field_owner=field,
        quantity=25,
        date=timezone.now().date()
    )

    test_rain_two = baker.make(
        rain_models.Rain,
        field_owner=field,
        quantity=40,
        date=timezone.now().date()
    )

    return {
        "rains": [test_rain_one, test_rain_two],
        "field": [field]
    }
