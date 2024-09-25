
from django.shortcuts import render
from .models import Animes


def anime_list(request):
    anime = Animes.objects.all()
    return render(request, 'animes/anime_list.html', {'animes': anime})


def index(request):
    return render(request, 'animes/index.html')
