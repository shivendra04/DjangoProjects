from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobsInfo(resquest):
    s='<h1>Hyderabad Jobs Infromation</h1>'
    return HttpResponse(s)

def punejobsInfo(resquest):
    s='<h1>Pune Jobs Infromation</h1>'
    return HttpResponse(s)

def chennaijobsInfo(resquest):
    s='<h1>Chennai Jobs Infromation</h1>'
    return HttpResponse(s)
