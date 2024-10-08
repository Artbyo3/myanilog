from django.urls import path
from django.contrib.auth import views as auth_views
from .views import user_anime_list

urlpatterns = [
    path('list/', user_anime_list, name='list'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]
