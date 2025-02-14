# Generated by Django 5.1.4 on 2025-01-08 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='institution_logos/')),
                ('theme_color', models.CharField(default='#ffffff', max_length=20)),
            ],
        ),
    ]
