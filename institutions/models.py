from django.db import models
from users.models import CustomUser

class Institution(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='institution_logos/')
    theme_color = models.CharField(max_length=20, default='#ffffff')
    users = models.ManyToManyField(CustomUser, related_name='institutions')

    def __str__(self):
        return self.name