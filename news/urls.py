from django.conf.urls import include
from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/comment/', views.comment, name='comment'),
    
    path('deletepost/<int:post_id>', views.deletepost, name="deletepost"),
    path('editpost/<int:post_id>/', views.editpost, name='editpost'),
    
    path('editcomment/<int:comment_id>/', views.editcomment, name='editcomment'), 
    path('deletecomment/<int:comment_id>', views.deletecomment, name="deletecomment"),
    
    path('searchdo/', views.search, name="search"),
    
    path('add/', views.add, name='add'),
    path('post/', views.post, name='post'),
    path('<int:post_id>', views.data, name='data'),
]
