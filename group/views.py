from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from itertools import groupby
from django.http import JsonResponse
from collections import Counter
#models
from .models import Group, Message
from django.contrib.auth.models import User
# Create your views here.
def index(request): 
    return render(request, "group/home.html", {'groups': Group.objects.all()})

def addpage(request): 
    return render(request, "group/add.html", {})

def addgroup(request): 
    if (request.method == "POST"):
        group=Group.objects.create(titlename=request.POST['title'],
                                   textcontent=request.POST['text'],
                                   admin=request.user)
        return redirect("/group/"+str(group.id))
        
def group(request, groupid): 
    group= get_object_or_404(Group, pk=groupid)
    message=Message.objects.filter(group=group)
    user_list=[]
    for message_item in message: 
        user_list.append(message_item.publisher)

    users= Counter(user_list)
    print(users)
    
    return render(request, "group/group.html",  {'group':group,'user': request.user, 'users': users})


class JsonListMessagesView(View): 
    def get(self,*args, **kwargs):
        groupid=kwargs.get('groupid')
        group=Group.objects.get(id=groupid)
        # for mm in Message.objects.all(): 
        #     mm.delete()
        message=list(Message.objects.filter(group=group).order_by('time')[:20].values()) # print(groupid)
        for message_item in message: 
            user=User.objects.get(id=message_item['publisher_id'])
            message_item["publisher"]=str(user)
        return JsonResponse({'data': message}, safe=False)
    

def delete(request, groupid): 
    group=Group.objects.get(pk= groupid)
    if (request.user==group.admin): 
        for m in Message.objects.filter(group=group): 
            m.delete()
        group.delete()
    return redirect("/group/")

def editgroupdata(request, groupid ):
    print("bad habtias ")
    group=get_object_or_404(Group, pk=groupid)
    if request.user == group.admin: 
        group.titlename=request.POST["title"]
        group.textcontent=request.POST["text"]
        group.save()
    return redirect("/group/" + str(groupid))


from collections import Counter
def search(request):        
    if request.method == 'GET': # this will be GET now      
        title_name =  request.GET.get('search') # do some research what it does       

        fuck = []
        for i in Group.objects.all(): 
            if title_name in i.titlename:
                fuck.append(i)
            # filter returns a list so you might consider skip except part

        for i in Group.objects.all(): 
            if title_name in i.textcontent:
                fuck.append(i)
            # filter returns a list so you might consider skip except part

        print("oh fuck -- ", fuck)
        lst=Counter(fuck)
    
        for l in lst: 
            l.title=l.titlename
            l.text=l.textcontent
            l.publisher=l.admin
        return render(request,"search.html",{'posts':lst, 'type': 'group'})
    else:
        return render(request,"search.html",{})


def sendmessage(request, groupid):      
    text=request.POST['text']
    print("text", text)
    print('group: ', groupid) 
    group=get_object_or_404(Group, pk=groupid)
    message=Message.objects.create(text=text, publisher=request.user, group=group)
    # messages=Message.objects.filter(group=group)
    # for i in messages: 
    #     i.delete()
    message.save()
    print('message', message)
    return JsonResponse( data=None, safe=False)

