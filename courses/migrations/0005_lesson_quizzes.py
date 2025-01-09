# Generated by Django 5.1.4 on 2025-01-09 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_instructor'),
        ('quizzes', '0002_alter_answer_question_alter_question_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='quizzes',
            field=models.ManyToManyField(blank=True, related_name='lessons', to='quizzes.question'),
        ),
    ]
