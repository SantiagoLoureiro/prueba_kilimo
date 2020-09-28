# Python imports
import pytest

# Django imports
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.mark.django_db
class TestRain:

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
