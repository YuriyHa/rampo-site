from django.db.models import fields
from django.forms import ModelForm, Textarea, widgets
from django.db import models

import datetime 
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model): 
    title = models.CharField(max_length=1000); 
    text = models.TextField(max_length=4000000)
    pub_date = models.DateTimeField('date published')
    publisher =models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
   
class Comment(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    publisher =models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 
    text = models.TextField(max_length=4000000)
    def __str__(self):
        return self.text
    
    
class CommentForm(ModelForm): 
    class Meta: 
        model = Comment
        fields= ('text',)
        widgets={
            'text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
