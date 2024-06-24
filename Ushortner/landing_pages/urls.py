from django.urls import path
from .views import landing_page_view, create_landing_page_view

urlpatterns = [
    path('create/', create_landing_page_view, name='create_landing_page'),
    path('<int:page_id>/', landing_page_view, name='landing_page'),]
