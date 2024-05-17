from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_view, name='shorten'),
    # path('<str:short_code>/', views.redirect_view, name='redirect'),
    # path('login/', LoginView.as_view(), name='login'),
]
