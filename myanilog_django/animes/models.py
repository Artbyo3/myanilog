import os
from django.utils.text import slugify
from django.db import models
from django.core.validators import MinValueValidator


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.genre_name
# END MODEL genre.

# New model for anime
# \Function to generate names for each anime.


def generate_filename(instance, filename):
    title = slugify(instance.title_romaji)
    ext = os.path.splitext(filename)[1]
    return f'anime_images/covers/{title}_cover{ext}'


class Anime(models.Model):
    id = models.AutoField(primary_key=True)
    title_romaji = models.CharField(max_length=50)
    title_english = models.CharField(max_length=50, blank=True)
    plot = models.TextField()
    episodes = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], null=True, blank=True)

    SEASON_CHOICES = [
        ('winter', 'Winter'),
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('fall', 'Fall'),
    ]
    season = models.CharField(max_length=6, choices=SEASON_CHOICES)

    ANIME_TYPE_CHOICES = [
        ('anime', 'Anime Series'),
        ('movie', 'Movie'),
        ('ova', 'Original Video Animation'),
        ('ona', 'Original Net Animation'),
        ('special', 'Special'),
    ]
    anime_type = models.CharField(max_length=24, choices=ANIME_TYPE_CHOICES)

    # score field maybe later.
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    studio = models.CharField(max_length=20, blank=True)
    cover_image = models.ImageField(
        upload_to=generate_filename, default='anime_images/covers/default_cover.jpg')

    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('finished', 'Finished'),
    ]
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='ongoing')

    # \ Model many to many with Genres model.
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title_romaji
    # END MODEL Animes.

    # python manage.py makemigrations
    # python manage.py migrate
