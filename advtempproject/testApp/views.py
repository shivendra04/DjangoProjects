from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'testApp/home.html')

def movies_view(request):
    return render(request,'testApp/movies.html')

def sports_view(request):
    return render(request,'testApp/sports.html')

def Politics_view(request):
    return render(request,'testApp/politics.html')
