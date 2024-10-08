from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserAnimeList


@login_required
def user_anime_list(request):
    user_animes_lists = UserAnimeList.objects.filter(user=request.user)
    return render(request, 'list.html', {'user_animes_lists': user_animes_lists})
