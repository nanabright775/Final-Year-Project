from django.urls import path
from . import views


#urls for bussiness card
urlpatterns = [
    path('create/', views.create_business_card, name='create_business_card'),
    path('business-cards/', views.business_card_list, name='business_card_list'),
    path('business-cards/<int:pk>/', views.business_card_detail, name='business_card_detail'),
    path('business-cards/update/<int:pk>/', views.business_card_update, name='business_card_update'),
    path('business-cards/delete/<int:pk>/', views.business_card_delete, name='business_card_delete'),
    path('<int:business_card_id>/render/', views.render_business_card, name='render_business_card'),
]


