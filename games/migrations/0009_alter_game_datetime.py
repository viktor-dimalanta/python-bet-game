# Generated by Django 4.2.1 on 2023-05-30 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_game_commentary_game_score_game_weather'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='datetime',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]