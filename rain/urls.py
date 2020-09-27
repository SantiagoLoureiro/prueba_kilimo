# Djagno imports
from django.urls import path

# Local imports
from rain import views

urlpatterns = [
    path(r'', views.RainView.as_view(), name='rain'),
]
