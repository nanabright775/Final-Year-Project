from django.urls import path
from . import views

app_name = 'portfolio_generator'

urlpatterns = [
    path('create_profile/', views.create_profile, name='create_profile'),
    path('choose_generation/', views.choose_generation, name='choose_generation'),
    path('list_portfolios/', views.list_portfolios, name='list_portfolios'),
    path('edit_portfolio/<int:portfolio_id>/', views.edit_portfolio, name='edit_portfolio'),
    path('<str:choice>/<str:username>/', views.display_generated_content, name='display_generated_content'),
]
