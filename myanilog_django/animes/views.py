from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Anime


# @cache_page(60 * 15)
class animes_list_view(ListView):
    model = Anime
    template_name = 'animes/index.html'
    context_object_name = 'all_animes'
    ordering = ["-id"]
    paginate_by = 9
    def get_queryset(self):
        return Anime.objects.prefetch_related('genres').all()


class anime_detail_view(DetailView):
    model = Anime
    template_name = 'animes/detail.html'
    context_object_name = "detail_anime"
