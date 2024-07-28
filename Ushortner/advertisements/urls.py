from django.urls import path
from . import views

#urls for campaign,Reels,likes,Comment
urlpatterns = [
    path('', views.content_list, name='content_list'),
    path('my-content/', views.my_content, name='my_content'),
    path('search/', views.search, name='search'),
    path('create/<str:content_type>/', views.content_create, name='content_create'),
    path('like/<int:content_type_id>/<int:object_id>/', views.like_content, name='like_content'),
    path('comment/<int:content_type_id>/<int:object_id>/', views.comment_content, name='comment_content'),
    path('<str:content_type>/<int:content_id>/', views.content_detail, name='content_detail'),
    path('update/<str:content_type>/<int:content_id>/', views.update_content, name='update_content'),
    path('delete/<str:content_type>/<int:content_id>/', views.delete_content, name='delete_content'),
 
]
