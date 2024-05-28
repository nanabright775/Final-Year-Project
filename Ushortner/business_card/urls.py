from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_business_card, name='create_business_card'),
    path('<int:business_card_id>/', views.business_card_detail, name='business_card_detail'),
]
