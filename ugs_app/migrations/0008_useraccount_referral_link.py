# Generated by Django 5.0.3 on 2024-06-16 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugs_app', '0007_alter_useraccount_referral_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='referral_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
