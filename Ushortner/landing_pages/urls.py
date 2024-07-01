from django.urls import path
from .views import landing_page_view, create_landing_page_view,user_landing_pages_view,update_landing_page_view,delete_landing_page_view, landing_page_detail

urlpatterns = [
    path('create/', create_landing_page_view, name='create_landing_page'),
    path('my-pages/', user_landing_pages_view, name='user_landing_pages'),
    path('<slug:slug>/', landing_page_view, name='landing_page'),
    path('landing/<slug:slug>/', landing_page_detail, name='landing_page_detail'),
    path('my-pages/update/<slug:slug>/', update_landing_page_view, name='update_landing_page'),
    path('my-pages/delete/<slug:slug>/', delete_landing_page_view, name='delete_landing_page'),
     
    ]
