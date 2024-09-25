from django.db import models

# New model for genres


class Genres(models.Model):
    id = models.AutoField(primary_key=True)
    Genre_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Genre_name


# New model for animes
class Animes(models.Model):
    # ADD id Auto
    title_romaji = models.CharField(max_length=255)
    title_english = models.CharField(max_length=255, blank=True)
    plot = models.TextField()
    episodes = models.PositiveIntegerField()
    season = models.CharField(max_length=50)
    # "ANIME" = Database entry, "anime" = Human reading value.
    anime_type = models.CharField(max_length=50, choices=[
                                  ('ANIME', 'Anime'), ('MOVIE', 'Movie')])
    # score field maybe later.
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    studio = models.CharField(max_length=100, blank=True)
    # cover_image = models.ImageField(upload_to='#', blank=True)
    # "ONGOING" = Database entry, "Ongoig" = Human reading value.
    status = models.CharField(max_length=50, choices=[
                              ('ONGOING', 'Ongoing'), ('FINISHED', 'Finished')], default='ONGOING')
    # Model many to many with Genres model.
    genres = models.ManyToManyField(Genres)

    def __str__(self):
        return self.title_romaji


# python manage.py makemigrations
# python manage.py migrate
