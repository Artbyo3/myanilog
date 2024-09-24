
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.index, name='animes_list'),
    path('detail', views.index, name='animes_detail'),
]
