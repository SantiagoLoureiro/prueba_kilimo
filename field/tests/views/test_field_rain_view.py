# Python imports
import pytest
from model_bakery import baker

# Django imports
from rest_framework.test import APIClient
from django.urls import reverse
from django.utils import timezone

# Local imports
from field import models as field_models
from rain import models as rain_models


@pytest.mark.django_db
class TestRain:

    @pytest.fixture
    def data_db(self):
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
            date=timezone.now()
        )

        test_rain_two = baker.make(
            rain_models.Rain,
            field_owner=field,
            quantity=40,
            date=timezone.now()
        )

        return {
            "rains": [test_rain_one, test_rain_two],
            "field": [field]
        }

    def test_rain_by_quantity_200(self, data_db):

        client = APIClient()
        url = reverse('field-rain')

        url = f"{url}?rain_quantity=20"

        field_db_test_one = data_db['field'][0]

        response = client.get(
            format='api',
            path=url,
        )

        response_data = response.data
        first_row = response_data[0]

        assert response.status_code == 200
        assert len(response_data) == 1
        assert first_row['name'] == field_db_test_one.name

    def test_rain_get_none_by_quantity_200(self, data_db):

        client = APIClient()
        url = reverse('field-rain')

        url = f"{url}?rain_quantity=100"

        response = client.get(
            format='api',
            path=url,
        )

        response_data = response.data

        assert len(response_data) == 0

    def test_rain_by_days_ago_rain_200(self, data_db):

        client = APIClient()
        url = reverse('field-rain')

        url = f"{url}?days_ago_rain=5"

        field_db_test_one = data_db['field'][0]

        response = client.get(
            format='api',
            path=url,
        )

        response_data = response.data
        first_row = response_data[0]

        assert response.status_code == 200
        assert len(response_data) == 1
        assert first_row['name'] == field_db_test_one.name

    def test_rain_get_by_days_ago_rain_400(self, data_db):

        client = APIClient()
        url = reverse('field-rain')

        url = f"{url}?days_ago_rain=8"

        response = client.get(
            format='api',
            path=url,
        )

        assert response.status_code == 400
