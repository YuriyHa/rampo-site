from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime
from .models import Post, Comment
from django.contrib.auth.models import User

# Create your views here.
def index(request): 
    latest_post = Post.objects.order_by('-pub_date')[:5]
    return render(request, 'home.html', {'post_list': latest_post, 'user': request.user})

def add(request): 
    if request.user.is_authenticated: 
        return render(request, "add.html", {'user': request.user})
    else: 
        return redirect("/signup/")

def post(request):
    if request.user.is_authenticated:  
        if request.method=="POST":  
            title = request.POST['title']
            text = request.POST['text']

            post=Post.objects.create(title=title, text=text, publisher=request.user, pub_date =datetime.now())
            post.save()
            post_id= post.id
            print('post has succesfuly saved: id -- ', post_id)
                
            return redirect('/news/' + str(post_id))
    else: 
        return redirect("/signup/")

def comment(request, post_id): 
    if request.method=="POST": 
        text=request.POST['text']
        user=request.user
        post = get_object_or_404(Post, pk=post_id)
        post.comment_set.create(text=text, publisher=user)
        post.save()
    
    return redirect('/news/' + str(post_id))

def data(request, post_id): 
    post = get_object_or_404(Post, pk=post_id)
    comments =Comment.objects.filter(Post = post)
    # for comment in comments: 
    #     comment.creator=False 
    #     if comment.publisher==request.user :
    #         comment.creator=True
    #     print(comment.creator)
    # print(comments)
        
    return render(request, 'data.html', {'post': post, 'comments': comments, 'iscreator': post.publisher==request.user, 'user': request.user})

def deletepost(request, post_id): 
    post = get_object_or_404(Post, pk=post_id)
    if post.publisher==request.user: 
        post.delete()
    return redirect("/news/") 

def editpost(request, post_id): 
    post = get_object_or_404(Post, pk=post_id)
    if post.publisher==request.user:     
        if request.method=="POST": 
            post.title=request.POST['title']
            post.text=request.POST['text']
            post.save()
            print("uspechno saved")
    return redirect('/news/' + str(post_id))   

def editcomment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.publisher:    
        if request.method=="POST":
            comment.text=request.POST['text']
            comment.save()
            print("uspechno saved")
    return redirect('/news/' + str(comment.Post.id))   

def deletecomment(request, comment_id): 
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.publisher:    
        comment.delete()
    return redirect('/news/' + str(comment.Post.id))    

from collections import Counter
def search(request):        
    if request.method == 'GET': # this will be GET now      
        title_name =  request.GET.get('search') # do some research what it does       

        fuck = []
        for i in Post.objects.all(): 
            if title_name in i.title:
                fuck.append(i)
            # filter returns a list so you might consider skip except part

        for i in Post.objects.all(): 
            if title_name in i.text:
                fuck.append(i)
            # filter returns a list so you might consider skip except part

        print("oh fuck -- ", fuck)
        lst=Counter(fuck)
    
        return render(request,"search.html",{'posts':lst, 'type': 'post'})
    else:
        return render(request,"search.html",{})
