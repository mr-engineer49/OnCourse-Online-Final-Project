# Generated by Django 5.1.4 on 2025-01-10 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='logo',
        ),
    ]
