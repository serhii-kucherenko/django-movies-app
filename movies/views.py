from django.shortcuts import get_object_or_404, render

from .models import Movie


def index(request):
    movies = Movie.objects.all()

    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    return render(request, 'movies/detail.html', {'movie': movie})
