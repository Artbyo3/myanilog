from django.db import models
# Missing line later
from animes.models import Animes


def UserAnimeList(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.
    anime = models.
    status = models.CharField(max_length=50, choises=[

        ('WATCHING', 'Watching'),
        ('COMPLETED', 'Completed'),
        ('DROPPED', 'Dropped'),
    ])


date_added = models.DateField(auto_now_add=True)

# Add non duplicated rule unique together
# Add def self.
