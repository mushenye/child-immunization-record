from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Child, Person, Vaccine, ImmunizationSchedule
from .serializers import CaregiverSerializer, ChildSerializer, VaccineSerializer, ImmunizationScheduleSerializer

class CaregiverViewset(viewsets.ModelViewSet):
    queryset=Person.objects.all()
    serializer_class=CaregiverSerializer


class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer

class ImmunizationScheduleViewSet(viewsets.ModelViewSet):
    queryset = ImmunizationSchedule.objects.all()
    serializer_class = ImmunizationScheduleSerializer
