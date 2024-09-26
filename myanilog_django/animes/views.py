
from django.shortcuts import render
from .models import Animes


def anime_list(request):
    animes = Animes.objects.all()
    return render(request, 'animes/index.html', {'animes': animes})
