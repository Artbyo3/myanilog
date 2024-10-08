from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


# ADD custom name funtion later.
    profile_picture = models.ImageField(
        upload_to='user_profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.username
