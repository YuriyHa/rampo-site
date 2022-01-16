from django.db import models
from django.db.models.fields import TextField
from django.forms import ModelForm, Textarea, widgets
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model): 
    admin=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    titlename=models.CharField(max_length=100)
    textcontent=models.CharField(max_length=1000)
    def __str__(self):
        return self.titlename
    
    

class Message(models.Model): 
    text = models.TextField(max_length=4000000)
    publisher=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    time=models.DateTimeField(auto_now_add=True)
    group=models.ForeignKey(Group, on_delete=models.SET_NULL,null=True, blank=True)
    def __str__(self):
        return str(self.time) + self.text
    

class MessageForm(ModelForm): 
    class Meta: 
        model=Message
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }