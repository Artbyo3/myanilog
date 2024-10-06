from django.views.generic import ListView
from .models import Anime


from django.shortcuts import render


class animes_list_view(ListView):
    model = Anime
    template_name = 'animes/index.html'
    context_object_name = 'all_animes'


def get_queryset(self):
    return Anime.objects.prefetch_related('Genre').all()
