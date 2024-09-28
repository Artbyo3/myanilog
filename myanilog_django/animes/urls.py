from django.urls import path
from .views import animes_list_view

urlpatterns = [
    path('', animes_list_view.as_view(), name='index'),
]
