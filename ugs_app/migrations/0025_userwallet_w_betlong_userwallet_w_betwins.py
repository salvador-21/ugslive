# Generated by Django 5.0.3 on 2024-08-15 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugs_app', '0024_remove_userwallet_w_betlong_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwallet',
            name='w_betlong',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='userwallet',
            name='w_betwins',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
