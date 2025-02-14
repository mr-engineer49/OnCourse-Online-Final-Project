# Generated by Django 5.1.4 on 2025-01-11 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0005_remove_institution_avaialble_institutions_and_more'),
        ('users', '0006_alter_updatecustomuser_available_institution_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatecustomuser',
            name='available_institution_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.availableinstitution'),
        ),
        migrations.AlterField(
            model_name='updatecustomuser',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.institution'),
        ),
    ]
