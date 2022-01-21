from django.urls import path, include
from . import views
from .views import JsonListMessagesView

app_name='group'
urlpatterns = [ 
    path("", views.index, name="index"), 
    path("<int:groupid>/", views.group, name="group"), 
    path("add/", views.addgroup, name="create"), 
    path("create/", views.addpage, name="addpage"), 
    path("group/search/", views.search, name="search"), 

    path("message-json/<int:groupid>", JsonListMessagesView.as_view(), name="message-json"), 
    path("sendmessage/<int:groupid>", views.sendmessage, name="sendmessage"), 
    path("delete/<int:groupid>", views.delete, name="delete"),
    path("editGroupData/<int:groupid>", views.editgroupdata, name="edit"),
    path("delete-message/<int:messageid>", views.deletemessage, name="deletemassage"),
]
 