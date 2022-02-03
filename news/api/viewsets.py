from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

from .mixin import PostMixin, CommentMixin
from rest_framework.decorators import action

class PostViewSet(PostMixin,viewsets.ModelViewSet): 
	queryset=Post.objects.all()
	serializer_class=PostSerializer
	permission_classes=(IsAuthenticatedOrReadOnly, )

class CommentViewSet(CommentMixin,viewsets.ModelViewSet): 
	queryset=Comment.objects.all()
	serializer_class=CommentSerializer
	permission_classes=(IsAuthenticatedOrReadOnly, )