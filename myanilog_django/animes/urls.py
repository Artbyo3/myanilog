
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('animes/', views.anime_list, name='animes_list'),
    path('detail', views.index, name='animes_detail'),
]
