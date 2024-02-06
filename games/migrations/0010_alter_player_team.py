# Generated by Django 4.2.1 on 2023-05-30 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_alter_game_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='games.team'),
        ),
    ]
