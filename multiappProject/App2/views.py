from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def AppInofo2(request):
    return HttpResponse('<h1>This is from Application 2</h1>')
