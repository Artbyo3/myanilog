from django.views.generic import ListView
from .models import Animes


class animes_list_view(ListView):
    model = Animes
    template_name = 'animes/index.html'
    context_object_name = 'animes'
