from django.shortcuts import render
from testApp.models import Company
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class CompanyListView(ListView):
    model=Company
class CompanyDetailView(DetailView):
    model=Company
class CompanyCreateView(CreateView):
    model=Company
    fields=('name','location','Ceo')
class CompanyUpdateView(UpdateView):
    model=Company
    fields=('name','Ceo')
class CompanyDeleteView(DeleteView):
    model=Company
    success_url=reverse_lazy('companies')#predefined
    #it will wait untill deletion completed
