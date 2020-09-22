from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
# Create your views here.
class Hellowordview(View):
    def get(self,request):
        return HttpResponse('<h1>this is form class based views</h1>')
class HellowordTemplateView(TemplateView):
    template_name='testApp/results.html'

class HellowordTemplateContext(TemplateView):
    template_name='testApp/emp.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='Shivendra'
        context['subject']='Python'
        context['marks']=100
        return context
