from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcomeView(request):
    print('This line printed by View function while processing request..')
    return HttpResponse('<h1>Custome MIDDLEWARE Demo</h1>')
