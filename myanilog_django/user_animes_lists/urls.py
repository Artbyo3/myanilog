from django.urls import path
from .views import user_anime_list

urlpatterns = [
    path('', user_anime_list, name='list'),
]
