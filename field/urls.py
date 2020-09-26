# Djagno imports
from django.conf.urls import url

# Local imports
from field import views

urlpatterns = [
    url(r'^field/rain/$', views.FieldRainView.as_view(), name='rain'),
]
