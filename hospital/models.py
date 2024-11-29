from django.db import models

from immunization_api.models import Person


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField()
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    website = models.URLField(blank=True, null=True)
    established_date = models.DateField()
    about = models.TextField()
    capacity = models.PositiveIntegerField(help_text="Total number of beds available")

    def __str__(self):
        return self.name



class Doctor(Person):
    hospital=models.ForeignKey(Hospital, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.fullname