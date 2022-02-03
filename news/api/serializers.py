from rest_framework import serializers

from ..models import Post, Comment
from .. import servises as serve_like

class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'text',
            'is_fan',
        )
    def get_is_fan(self, obj):
        user=self.context.get('request').user
        return serve_like.is_fan(obj, user)


from django.contrib.auth import get_user_model

User = get_user_model()
class FanSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = (
            'username',
            'full_name',
        )
    def get_full_name(self, obj):
        return obj.get_full_name()

class CommentSerializer(serializers.ModelSerializer): 
	#is_fan for comments
	pub_user_name=serializers.SerializerMethodField()
	is_fan=serializers.SerializerMethodField()
	post_title=serializers.SerializerMethodField()
	class Meta: 
		model=Comment
		fields=(
			'id', 
			'text', 
			'publisher', 
			'pub_user_name', 
			'Post_id', 
			'post_title', 
			'is_fan', 
		)

	def get_is_fan(self, obj): 
		if (self.context.get('request')):
			user=self.context.get('request').user
			return serve_like.is_fan(obj,user)
		else: 
			return 'use another link "/comment/[comment-id]"'
	def get_post_title(self, obj): 
		return str(obj.Post.title)
	def get_pub_user_name(self, obj): 
		if obj.publisher != None: 
			return str(obj.publisher.username)
		else: 
			return "None"
