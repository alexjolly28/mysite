# Generated by Django 2.2 on 2019-10-11 18:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_movie_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
