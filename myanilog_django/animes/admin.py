from django.contrib import admin
from .models import Anime, Genre

class AnimeAdmin(admin.ModelAdmin):
	list_display = ('title_romaji','anime_type' ,'status', 'season','episodes','studio')
	ordering = ('-id',)

admin.site.register(Anime, AnimeAdmin)

admin.site.register(Genre)
