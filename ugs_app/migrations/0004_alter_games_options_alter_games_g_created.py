# Generated by Django 5.0.3 on 2024-06-14 14:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugs_app', '0003_alter_games_g_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='games',
            options={'get_latest_by': ('-g_created',)},
        ),
        migrations.AlterField(
            model_name='games',
            name='g_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
