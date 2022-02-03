from rest_framework import routers
from .viewsets import PostViewSet, CommentViewSet
from django.urls import path, include, re_path


router=routers.SimpleRouter()
app_name='post-api'
router.register(prefix=r'post', viewset=PostViewSet)
router.register(prefix=r'comment' , viewset=CommentViewSet)

urlpatterns =router.urls