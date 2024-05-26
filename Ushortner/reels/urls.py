from django.urls import path
from . import views

urlpatterns = [
    path('', views.reel_list, name='reel_list'),
    path('my-reels/', views.my_reels, name='my_reels'),
    path('upload/', views.reel_upload, name='reel_upload'),
    path('update/<int:reel_id>/', views.reel_update, name='reel_update'),
    path('delete/<int:reel_id>/', views.reel_delete, name='reel_delete'),
    # path('<int:reel_id>/', views.campaign_detail, name='campaign_detail'),
]
