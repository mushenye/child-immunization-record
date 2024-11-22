from django.contrib import admin

from immunization_api.models import Caregiver, Child

# Register your models here.
admin.site.register(Caregiver)
admin.site.register(Child)