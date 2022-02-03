from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from .models import Like,Post, Comment

from datetime import datetime

User=get_user_model()

def editcomment(user,obj,data)->bool: 
	if obj.publisher==user: 
		obj.text=data['text']
		obj.save()
		return True
	else: 
		return False

def comment(user,obj,data): 
	Comment.objects.create(text=data['text'],publisher=user,Post=obj)

def editpost(user,obj,data) -> bool:
	if obj.publisher==user: 
		obj.title=data['title']
		obj.text=data['text']
		obj.save() 
		return True
	else: 
		return False 


def deleteModel(user, obj) -> bool: 
	if obj.publisher == user: 
		obj.delete()
		return True
	else: 
		return False


def post(user, data): 
	Post.objects.create(title=data['title'], text=data['text'], pub_date=str(datetime.now()), publisher=user)

def add_like(obj, user): 
	obj_type=ContentType.objects.get_for_model(obj)
	like, is_created=Like.objects.get_or_create(content_type=obj_type, object_id=obj.id, user=user)
	return like

def remove_like(obj, user): 
	obj_type=ContentType.objects.get_for_model(obj)
	Like.objects.filter(content_type=obj_type, object_id=obj.id, user=user).delete()


def is_fan(obj, user) -> bool: 
	if not user.is_authenticated: 
		return False
	obj_type=ContentType.objects.get_for_model(obj)
	likes=Like.objects.filter(content_type=obj_type, object_id=obj.id, user=user)
	return likes.exists()

def get_fans(obj): 
	obj_type=ContentType.objects.get_for_model(obj)
	return User.objects.filter(likes__content_type=obj_type, likes__object_id=obj.id)

def get_comments(obj, user): 
	return Comment.objects.filter(Post=obj)
