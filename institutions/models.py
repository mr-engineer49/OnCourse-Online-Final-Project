from django.db import models

class Institution(models.Model):
    name = models.CharField(max_length=200)
    theme_color = models.CharField(max_length=20, default='#ffffff')
    users = models.ManyToManyField('users.CustomUser', related_name='institutions')

    def __str__(self):
        return self.name