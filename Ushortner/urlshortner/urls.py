from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_view, name='shorten'),
]
