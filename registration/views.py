from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from chat.models import UserProfile

from django.contrib.auth.models import User
from news.models import Post
from chat.models import Friends, UserProfile
from group.models import Group

def SignUp(request):
    """
    Sign up view
    :param request:
    :return:
    """
    message = []
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.validate_email()
            username = form.validate_username()
            password = form.validate_password()
            if not email:
                message.append("Email already registered!")
            elif not password:
                message.append("Passwords don't match!")
            elif not username:
                message.append("Username already registered!")
            else:
                print("SUCCESS!!!!")
                form.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                profile = UserProfile(email=email, name=name, username=username)
                profile.save()
                return redirect("/")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form, "heading": "Sign Up", "message": message})

def userdata(request, username):
    user=get_object_or_404(User, username=username)
    
    post=Post.objects.filter(publisher=user).order_by('-pub_date')
    
    userprofile =get_object_or_404(UserProfile, username=username)
    frend_id=Friends.objects.filter(user=userprofile)
    frend=[]
    for id in frend_id: 
        frend.append(get_object_or_404(UserProfile, id=id.friend))
        
    group=Group.objects.filter(admin=user)
    
    
    
    return render(request, "registration/userdata.html", {'user': user
                                                          , 'posts':post
                                                          , 'thisuser':request.user
                                                          , 'frends': frend
                                                          , 'groups':group}) 
    

def delete(request, username): 
    user=User.objects.get(username=username)
    userpr = UserProfile.objects.get(username=username)
    if request.user == user: 
        for post in Post.objects.filter(publisher=user): post.delete()
        for group in Group.objects.filter(admin=user): group.delete()

        print(user)
        userpr.delete()
        print("user-pr deleted...")
        user.delete()
        print("user is deleted...")
        return redirect("/")
    else:  
        return redirect("/")

