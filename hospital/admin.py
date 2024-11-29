from django.contrib import admin
from .models import Hospital

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'established_date', 'capacity')
    search_fields = ('name', 'departments', 'services')
    list_filter = ('established_date',)

