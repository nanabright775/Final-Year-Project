from django.urls import path
# from user.views import signup
from .views import (
    signup_view,
    login_view,
    logout_view,
    user_dashboard,
    redirect_view,
    analytics_view,
    url_details_view,
)


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('userdashboard/', user_dashboard, name='userdashboard'),
    path('analytics/', analytics_view, name='analytics_view'),
    path('<short_code>/', redirect_view, name='redirect_view'),
    path('details/<short_code>/', url_details_view, name='url_details_view'),

    # path('<str:short_code>/', views.redirect_to_original, name='redirect_to_original'),
]