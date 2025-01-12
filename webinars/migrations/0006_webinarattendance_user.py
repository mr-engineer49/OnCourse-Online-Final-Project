# Generated by Django 5.1.4 on 2025-01-12 12:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webinars', '0005_remove_webinarattendance_participants'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='webinarattendance',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='webinar_attendances', to=settings.AUTH_USER_MODEL),
        ),
    ]
