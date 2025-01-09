# Generated by Django 5.1.4 on 2025-01-09 15:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
