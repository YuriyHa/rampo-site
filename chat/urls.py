from django.urls import path, include
from . import views

urlpatterns = [
    path("chat/", views.openchat, name="index"),
    path("", views.index, name="openchat"),
    path("search/", views.search, name="search"),
    path("addfriend/<str:name>", views.addFriend, name="addFriend"),
    path("chat/<str:username>", views.chat, name="chat"),
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('api/messages', views.message_list, name='message-list'), 
]
