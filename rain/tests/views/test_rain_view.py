# Python imports
import pytest
from model_bakery import baker

# Django imports
from rest_framework.test import APIClient
from django.urls import reverse
from django.utils import timezone

# Local improts
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
            quantity=25
        )

        test_rain_two = baker.make(
            rain_models.Rain,
            field_owner=field,
            quantity=12
        )

        return {
            "rains": [test_rain_one, test_rain_two],
            "field": [field]
        }

    def test_rain_view_get_status_200(self, data_db):

        client = APIClient()
        url = reverse('rain')
        response = client.get(url)

        response_data = response.data[0]

        rain_db_test_one = data_db['rains'][0]
        rain_db_test_two = data_db['rains'][1]
        field_db_test_one = data_db['field'][0]

        rain_response_test_one = response_data[0]
        rain_response_test_two = response_data[1]

        assert len(response_data) == 2
        assert str(rain_db_test_one.date) == rain_response_test_one['date']
        assert str(rain_db_test_two.date) == rain_response_test_two['date']
        assert field_db_test_one.id == rain_response_test_one['field_owner']
        assert field_db_test_one.id == rain_response_test_two['field_owner']

    def test_rain_view_post_status_200(self, data_db):

        client = APIClient()
        url = reverse('rain')
        quantity = 12465.32

        field_db_test_one = data_db['field'][0]
        data = {
            "date": str(timezone.now().date()),
            "quantity": quantity,
            "field_owner": field_db_test_one.id
        }

        response = client.post(
            path=url,
            data=data
        )

        rain_qs = rain_models.Rain.objects.filter(
            quantity=quantity
        )

        assert response.status_code == 201
        assert response.data == data
        assert rain_qs.exists()

    def test_rain_view_post_status_400(self, data_db):

        client = APIClient()
        url = reverse('rain')
        data = {
        }

        response = client.post(
            path=url,
            data=data
        )

        assert response.status_code == 400

