from rest_framework import serializers
from .models import Child, Vaccine, ImmunizationSchedule

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = '__all__'

class ImmunizationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImmunizationSchedule
        fields = '__all__'
