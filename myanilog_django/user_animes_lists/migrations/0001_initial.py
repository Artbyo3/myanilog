# Generated by Django 5.1.1 on 2024-10-07 00:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animes', '0004_alter_anime_anime_type_alter_anime_season_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnimeList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('watching', 'Watching'), ('completed', 'Completed'), ('dropped', 'Dropped'), ('on_hold', 'On Hold'), ('plan_to_watch', 'Plan to Watch')], max_length=13)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('rating', models.PositiveIntegerField(blank=True, choices=[(1, '1'), (2, '1'), (3, '1'), (4, '1'), (5, '1'), (6, '1'), (7, '1'), (8, '1'), (9, '1'), (10, '1')], null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animes.anime')),
                ('favorites', models.ManyToManyField(blank=True, related_name='favorited_by', to='animes.anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'indexes': [models.Index(fields=['status'], name='user_animes_status_8f5e47_idx'), models.Index(fields=['date_added'], name='user_animes_date_ad_29d6e7_idx')],
                'unique_together': {('user', 'anime')},
            },
        ),
    ]
