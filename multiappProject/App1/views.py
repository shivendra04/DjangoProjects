from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def AppInofo1(request):
    return HttpResponse('<h1>This is from Application 1</h1>')
