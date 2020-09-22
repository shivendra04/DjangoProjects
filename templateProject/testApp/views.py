from django.shortcuts import render
import datetime

# Create your views here.
def tempview(request):
    return render(request,'testApp/wish.html')
