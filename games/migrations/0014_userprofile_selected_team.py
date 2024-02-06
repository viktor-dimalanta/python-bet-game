# Generated by Django 4.2.1 on 2023-06-01 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0013_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='selected_team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='games.team'),
            preserve_default=False,
        ),
    ]
