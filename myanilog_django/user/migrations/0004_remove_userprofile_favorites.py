# Generated by Django 5.1.1 on 2024-10-07 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_userprofile_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='favorites',
        ),
    ]
