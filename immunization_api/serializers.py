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
    
    due_date = serializers.DateField(read_only=True)

    class Meta:
        model = ImmunizationSchedule
        fields = [
            'id',
            'date_created',
            'child_weight',
            'child',
            'vaccine',
            'alert_sent',
            'due_date',
        ]
        # Optionally, make some fields read-only if necessary
        read_only_fields = ['id', 'date_created', 'due_date']
