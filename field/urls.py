# Djagno imports
from django.urls import path

# Local imports
from field import views

urlpatterns = [
    path(r'rain/', views.FieldRainView.as_view(), name='field-rain'),
]
