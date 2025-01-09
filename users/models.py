from django.db import models
from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):
    is_instructor = models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)
    is_learner = models.BooleanField(default=True)