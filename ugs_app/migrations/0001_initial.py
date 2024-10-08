# Generated by Django 5.0.3 on 2024-06-14 12:38

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fight',
            fields=[
                ('f_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('f_number', models.IntegerField(blank=True, null=True)),
                ('f_winner', models.CharField(blank=True, max_length=100)),
                ('f_status', models.CharField(choices=[('OPEN', 'OPEN'), ('CLOSED', 'CLOSE'), ('DONE', 'DONE'), ('LAST CALL', 'LAST CALL')], max_length=50, null=True)),
                ('f_update', models.DateTimeField(auto_now=True)),
                ('f_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-f_created'],
            },
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('g_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('g_name', models.CharField(blank=True, max_length=50)),
                ('g_redname', models.CharField(blank=True, max_length=50)),
                ('g_bluename', models.CharField(blank=True, max_length=50)),
                ('g_plasada', models.DecimalField(decimal_places=3, default=0.0, max_digits=5)),
                ('g_desc', models.CharField(blank=True, max_length=100)),
                ('g_category', models.CharField(choices=[('E-SABONG', 'E-SABONG'), ('BALL GAMES', 'BALL GAMES'), ('PERYA', 'PERYA')], max_length=50, null=True)),
                ('g_link', models.CharField(blank=True, max_length=100)),
                ('g_image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('g_status', models.CharField(choices=[('OPEN', 'OPEN'), ('CLOSED', 'CLOSED')], default='CLOSED', max_length=50)),
                ('g_by', models.CharField(blank=True, max_length=100)),
                ('g_update', models.DateTimeField(auto_now=True)),
                ('g_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ('-g_created',),
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.CharField(blank=True, max_length=100)),
                ('category', models.CharField(choices=[('MERON', 'MERON'), ('WALA', 'WALA'), ('DRAW', 'DRAW'), ('LONGEST', 'LONGEST')], max_length=50, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('WIN', 'WIN'), ('LOSE', 'LOSE')], default='PENDING', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('player', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL)),
                ('fight', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='fight', to='ugs_app.fight')),
            ],
        ),
        migrations.AddField(
            model_name='fight',
            name='f_game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game', to='ugs_app.games'),
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', models.CharField(default='00000000000', max_length=11, null=True)),
                ('referral_code', models.CharField(blank=True, max_length=100, null=True)),
                ('usertype', models.CharField(choices=[('SUPER ADMIN', 'SUPER ADMIN'), ('ADMIN', 'ADMIN'), ('DECLARATOR', 'DECLARATOR'), ('LOADER', 'LOADER'), ('AGENT', 'AGENT'), ('PLAYER', 'PLAYER')], default='ADMIN', max_length=50)),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('BANNED', 'BANNED')], default='ACTIVE', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_agent', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='agent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserWallet',
            fields=[
                ('w_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('w_balance', models.IntegerField(blank=True, default=0)),
                ('w_points', models.IntegerField(blank=True, default=0)),
                ('w_commission', models.IntegerField(blank=True, default=0)),
                ('w_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('BANNED', 'BANNED')], max_length=50)),
                ('w_dateupdate', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userwallet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
