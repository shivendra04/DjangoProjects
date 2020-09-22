from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def timeInfo(request):
    date=datetime.datetime.now()
    msg='<h1>Hello Friends Good Evening!!</h1>'
    msg=msg+'<h1>Now The Server Time is:'+str(date)+'</h1>'
    return HttpResponse(msg)
