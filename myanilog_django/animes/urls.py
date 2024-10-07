from django.urls import path
from .views import animes_list_view
from .views import anime_detail_view

urlpatterns = [
    path('', animes_list_view.as_view(), name='index'),
    path('anime/<int:pk>/', anime_detail_view.as_view(), name='anime_detail'),
]
