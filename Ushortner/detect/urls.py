# detect/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.detect_link, name='detect_link'),
]
