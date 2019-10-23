from django.shortcuts import render , get_object_or_404

# Create your views here.
from django.http import HttpResponse ,Http404
from .models import Movie


def index(request):
    return render(request, 'mysite/index.html')


def home(request):
    movies = Movie.objects.all()
    output = ','.join([m.title for m in movies])
    return render(request, 'mysite/home.html', {'movies': movies})


def detail(request, movie_id):
    movie=get_object_or_404(Movie,pk=movie_id)
    return render(request,'mysite/details.html',{'movie':movie})
