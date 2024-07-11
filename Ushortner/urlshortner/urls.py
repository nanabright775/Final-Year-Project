from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_view, name='shorten'),
    path('api-documentation/', views.api_documentation, name='api_documentation'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('landingpage/', views.landingpage, name='landingpage'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
]
