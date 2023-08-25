from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def Insert_Topic(request):
    kr=input('Enter topic_name: ')
    to=topic.objects.get_or_create(topic_name=kr)[0]
    to.save()
    return HttpResponse('data is inserted')
def Insert_webpage(request):
    kr=input('Enter Topic_name: ')
    to=topic.objects.get_or_create(topic_name=kr)[0]
    to.save()
    n=input('Enter name: ')
    u=input('Enter url: ')
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    return HttpResponse('data inserted')
def Insert_Access(request):
    kr=input('Enter Topic_name: ')
    to=topic.objects.get_or_create(topic_name=kr)[0]
    to.save()
    n=input('Enter name: ')
    u=input('Enter url: ')
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    d=input('Enter date: ')
    a=input('Enter authorname: ')
    ao=Accessrecords.objects.get_or_create(name=wo,date=d,author=a)[0]
    ao.save()
    return HttpResponse('data is Inserted')


