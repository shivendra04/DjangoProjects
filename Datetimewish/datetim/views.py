from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def DatetimeInfo(response):
    x = datetime.datetime.now()
    h=int(x.strftime("%H"))
    msg='<h1>Hello Guest Very '
    if h<12:
        msg=msg+'Good Morning'
    elif h<16:
            msg=msg+'Good AfterNoon'
    elif h<21:
            msg=msg+'Good Evening'
    else:
        msg=msg+'Good Night'
    '</h1>'
    msg=msg+'<h1>Server Time is '+str(datetime.datetime.now())+ '</h1>'
    return HttpResponse(msg)
