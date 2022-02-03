from django.db.models import fields
from django.forms import ModelForm, Textarea, widgets
from django.db import models

import datetime 
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
# Create your models here.
class Like(models.Model): 
    user=models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)
    content_type=models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')

class Post(models.Model): 
    title = models.CharField(max_length=1000); 
    text = models.TextField(max_length=4000000)
    pub_date = models.DateTimeField('date published')
    publisher =models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    likes = GenericRelation(Like)
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
    @property
    def total_likes(self):
        return self.likes.count()
    


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('text', )
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
   
class Comment(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    publisher =models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 
    text = models.TextField(max_length=4000000)
    likes = GenericRelation(Like)

    def __str__(self):
        return self.text

    @property
    def total_likes(self): 
        return self.likes.count()
    
    
class CommentForm(ModelForm): 
    class Meta: 
        model = Comment
        fields= ('text',)
        widgets={
            'text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
