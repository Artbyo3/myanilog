import os
from django.db import models


class Genres(models.Model):
    id = models.AutoField(primary_key=True)
    Genre_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.Genre_name
# END MODEL Genres.


# New model for animes
# \Function to generate names for each anime.
def generate_filename(instance, filename):
    title = instance.title_romaji.replace(" ", "_")
    ext = os.path.splitext(filename)[1]
    return f'anime_images/covers/{title}_cover{ext}'


class Animes(models.Model):
    id = models.AutoField(primary_key=True)
    title_romaji = models.CharField(max_length=50)
    title_english = models.CharField(max_length=50, blank=True)
    plot = models.TextField()
    episodes = models.PositiveIntegerField()

    SEASON_CHOICES = [
        ('WINTER', 'Winter'),
        ('SPRING', 'Spring'),
        ('SUMMER', 'Summer'),
        ('FALL', 'Fall'),
    ]
    season = models.CharField(max_length=6, choices=SEASON_CHOICES)

    ANIME_TYPE_CHOICES = [
        ('ANIME', 'Anime Series'),
        ('MOVIE', 'Movie'),
        ('OVA', 'Original Video Animation'),
        ('ONA', 'Original Net Animation'),
        ('SPECIAL', 'Special'),
    ]
    anime_type = models.CharField(max_length=50, choices=ANIME_TYPE_CHOICES)

    # score field maybe later.
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    studio = models.CharField(max_length=20, blank=True)
    cover_image = models.ImageField(
        upload_to=generate_filename, default='anime_images/covers/default_cover.jpg')

    # "ONGOING" = Database entry, "Ongoig" = Human reading value.
    STATUS_CHOISES = [
        ('ONGOING', 'Ongoing'),
        ('FINISHED', 'Finished'),
    ]
    status = models.CharField(
        max_length=20, choices=STATUS_CHOISES, default='ONGOING')

    # \ Model many to many with Genres model.
    genres = models.ManyToManyField(Genres)

    def __str__(self):
        return self.title_romaji
    # END MODEL Animes.

    # python manage.py makemigrations
    # python manage.py migrate
