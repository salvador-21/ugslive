# Generated by Django 5.0.3 on 2024-08-17 17:55

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StakeSlot',
            fields=[
                ('s_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('s_name', models.CharField(blank=True, default=0, max_length=50)),
                ('s_rate', models.IntegerField(blank=True, default=0)),
                ('s_amount', models.IntegerField(blank=True, default=0)),
                ('s_duration', models.IntegerField(blank=True, default=0)),
                ('s_date', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
