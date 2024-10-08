# Generated by Django 5.1.1 on 2024-10-07 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0003_rename_genre_anime_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='anime_type',
            field=models.CharField(choices=[('anime', 'Anime Series'), ('movie', 'Movie'), ('ova', 'Original Video Animation'), ('ona', 'Original Net Animation'), ('special', 'Special')], max_length=24),
        ),
        migrations.AlterField(
            model_name='anime',
            name='season',
            field=models.CharField(choices=[('winter', 'Winter'), ('spring', 'Spring'), ('summer', 'Summer'), ('fall', 'Fall')], max_length=6),
        ),
        migrations.AlterField(
            model_name='anime',
            name='status',
            field=models.CharField(choices=[('ongoing', 'Ongoing'), ('finished', 'Finished')], default='ONGOING', max_length=20),
        ),
    ]
