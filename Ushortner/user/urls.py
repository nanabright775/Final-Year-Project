from django.urls import path, include
from .views import (
    signup_view,
    login_view,
    logout_view,
    user_dashboard,
    redirect_view,
    analytics_view,
    url_details_view,
    customize_short_url_view,
    generate_qr_code_view,
    delete_short_url,
    user_links,
)
from chat import views

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('userdashboard/', user_dashboard, name='userdashboard'),
    path('analytics/', analytics_view, name='analytics_view'),
    path('customize/', customize_short_url_view, name='customize_short_url'),
    path('generate_qr_code/', generate_qr_code_view, name='generate_qr_code'),
    path('campaign/', include('campaign.urls')), 
    path('chat/', include('chat.urls')),
    path('links/', user_links, name='user_links'),
    path('reels/', include('reels.urls')),
    path('business_card/', include('business_card.urls')),
    path('detect/', include('detect.urls')),
    path('<short_code>/', redirect_view, name='redirect_view'),
    path('details/<short_code>/', url_details_view, name='url_details_view'),
    path('<str:short_code>/delete/', delete_short_url, name='delete_short_url'),

]