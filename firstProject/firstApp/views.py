from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome(request):
    # inside any name is fine
    #return HttpResponse(s)
    s='<h1>Welcome to Django Class.</h1>'
    return HttpResponse(s)
