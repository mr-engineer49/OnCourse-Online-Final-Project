from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from institutions.models import AvailableInstitution, Institution





class CustomUser(AbstractUser):
    institution_works_for = models.ForeignKey(
        'institutions.Institution', on_delete=models.SET_NULL, null=True, blank=True
    )
    available_institutions = models.ManyToManyField(
        'institutions.AvailableInstitution', blank=True
    )
    is_instructor = models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)
    is_learner = models.BooleanField(default=False)
    is_learn_instructor = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # Unique related_name for CustomUser
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions_set",  # Unique related_name for CustomUser
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )


    def __str__(self):
        # Ensure username always returns a string
        return self.username if self.username else "Unnamed User"


class UpdatedUser(AbstractUser):
    institution_works_for = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True, blank=True, related_name='institution_users')
    available_institutions = models.ManyToManyField(AvailableInstitution, blank=True, related_name='available_institution_users')
    is_instructor = models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)
    is_learner = models.BooleanField(default=True)


    def __str__(self):
        return self.username if self.username else "Unnamed User"



