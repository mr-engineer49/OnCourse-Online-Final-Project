from django.db import models

class Institution(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    theme_color = models.CharField(max_length=20, default='#ffffff')
    users = models.ManyToManyField('users.CustomUser', related_name='institution_users')

    def __str__(self):
        return self.name or 'Unnamed Institution'
    

class AvailableInstitution(models.Model):
    available_institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='available_institutions')

    def __str__(self):
        return self.available_institution.name or 'Unnamed Institution'