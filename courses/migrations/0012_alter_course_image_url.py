# Generated by Django 4.2.18 on 2025-01-27 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_course_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image_url',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='courses/'),
        ),
    ]
