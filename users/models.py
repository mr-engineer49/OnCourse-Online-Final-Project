from django.db import models
from django.contrib.auth.models import AbstractUser
from institutions.models import Institution




class CustomUser(AbstractUser):
    is_instructor = models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)
    is_learner = models.BooleanField(default=True)
    institution = models.ForeignKey('institutions.Institution', on_delete=models.CASCADE, related_name='courses', default='')
    def __str__(self):
        return self.username
