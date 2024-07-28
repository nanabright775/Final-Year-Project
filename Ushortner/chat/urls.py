from django.urls import path
from . import views

#urls for chatting
urlpatterns = [    
    path('', views.chat_list, name='chat_list'),
    path('<str:username>/', views.chat_detail, name='chat_detail'),
    path('delete_chat/<int:user_id>/', views.delete_chat, name='delete_chat'),
]
