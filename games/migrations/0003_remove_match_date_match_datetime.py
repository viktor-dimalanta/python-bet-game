# Generated by Django 4.2.1 on 2023-05-27 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_player_age_player_college_player_player_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='date',
        ),
        migrations.AddField(
            model_name='match',
            name='datetime',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
