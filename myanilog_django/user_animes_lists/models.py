from django.db import models
from animes.models import Anime
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAnimeList(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    STATUS_CHOICES = [
        ('watching', 'Watching'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped'),
        ('on_hold', 'On Hold'),
        ('plan_to_watch', 'Plan to Watch'),
    ]
    # Corrección en 'choices'
    status = models.CharField(max_length=13, choices=STATUS_CHOICES)
    favorites = models.ManyToManyField(
        Anime, related_name='favorited_by', blank=True)
    date_added = models.DateField(auto_now_add=True)

    rating = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 11)], null=True, blank=True)

    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'anime')
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['date_added']),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.anime.title_romaji} ({self.status})"
