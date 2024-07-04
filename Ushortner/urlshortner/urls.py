from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_view, name='shorten'),
    path('api-documentation/', views.api_documentation, name='api_documentation'),
]
