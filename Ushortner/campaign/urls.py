from django.urls import path
from .views import campaign_list, campaign_create, my_campaigns, delete_campaign, update_campaign, campaign_detail

urlpatterns = [
    path('list', campaign_list, name='campaign_list'),
    path('new/', campaign_create, name='campaign_create'),
    path('my_campaign/', my_campaigns, name='my_campaigns'),
    path('campaign/<int:campaign_id>/delete/', delete_campaign, name='delete_campaign'),
    path('campaign/<int:campaign_id>/update/', update_campaign, name='update_campaign'),
    path('campaign/<int:campaign_id>/', campaign_detail, name='campaign_detail'),
]
