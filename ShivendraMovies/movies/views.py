from django.shortcuts import render
from movies.models import Movie
from movies import forms


# Create your views here.
def index_view(request):
    return render(request,'movies/index.html')

def add_movie_view(request):
    form=forms.MoviesForm()
    if request.method=='POST':
        form=forms.MoviesForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)
    return render(request,'movies/addmovies.html',{'form':form})


def list_movie_view(request):
    movie_list=Movie.objects.all()
    return render(request,'movies/listmovies.html',{'movie_list':movie_list})
