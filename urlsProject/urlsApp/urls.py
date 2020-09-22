from django.urls import path
from urlsApp import views
urlpatterns = [
    path('hydjobs/', views.hydjobsInfo),
    path('punejobs/', views.punejobsInfo),
    path('chennaijobs/', views.chennaijobsInfo),
]
