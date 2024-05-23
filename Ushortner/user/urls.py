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


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('userdashboard/', user_dashboard, name='userdashboard'),
    path('analytics/', analytics_view, name='analytics_view'),
    path('customize/', customize_short_url_view, name='customize_short_url'),
    path('generate_qr_code/', generate_qr_code_view, name='generate_qr_code'),
    path('campaign/', include('campaign.urls')),  # Add this line
    path('links/', user_links, name='user_links'),
    path('<short_code>/', redirect_view, name='redirect_view'),
    path('details/<short_code>/', url_details_view, name='url_details_view'),
    path('<str:short_code>/delete/', delete_short_url, name='delete_short_url'),

    # path('<str:short_code>/', views.redirect_to_original, name='redirect_to_original'),
]