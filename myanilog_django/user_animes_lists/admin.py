from django.contrib import admin

from .models import UserAnimeList


class UserAnimeListAdmin(admin.ModelAdmin):

    list_display = ('user', 'anime', 'status', 'rating',)

    search_fields = ('user__username', 'anime__title')
    list_filter = ('status',)


admin.site.register(UserAnimeList, UserAnimeListAdmin)
