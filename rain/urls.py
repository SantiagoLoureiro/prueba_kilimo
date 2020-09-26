# Djagno imports
from django.conf.urls import url

# Local imports
from rain import views

urlpatterns = [
    url(r'^rain/$', views.RainView.as_view(), name='rain'),
]
