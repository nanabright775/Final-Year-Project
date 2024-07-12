# detect/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path('detect/', views.form_page, name='form_page'),
    path('', views.predict, name='predict'),
]
