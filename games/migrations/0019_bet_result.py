# Generated by Django 4.2.1 on 2023-06-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0018_bet_team_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='result',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
