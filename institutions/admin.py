from django.contrib import admin

from institutions.models import AvailableInstitution, Institution

# Register your models here.

admin.site.register(Institution)
admin.site.register(AvailableInstitution)

