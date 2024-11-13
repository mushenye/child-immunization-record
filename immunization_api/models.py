from django.db import models

from django.db import models
from django.utils import timezone
from datetime import date
from dateutil.relativedelta import relativedelta

class Person(models.Model):
    date_created=models.DateField(auto_now=True)
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    @property
    def fullname(self):
        return  '{} {} {}'.format(self.first_name,self.middle_name, self.last_name)

    def __str__(self):
        return self.fullname

class Parent(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    email_address=models.EmailField()
    parent_phone_number = models.CharField(max_length=15)  
    parent_type=models.CharField(choices=[('Father','Father'), ('Mother','Mother')], max_length=50)



    def __str__(self):
        return self.person.fullname()

    

class Child(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    parent =models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='parent')
    birth_date = models.DateField()
    birth_weight=models.IntegerField()
    

    def __str__(self):
        return self.person.fullname()    
    

class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_months_after_birth = models.IntegerField(help_text="Months after birth when this vaccine is due.")

    def __str__(self):
        return self.name

class ImmunizationSchedule(models.Model):
    date_created=models.DateField(auto_now_add=True)
    child_weight=models.IntegerField()
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    alert_sent = models.BooleanField(default=False)

    @property
    def due_date(self):
        return self.child.birth_date + relativedelta(months=self.vaccine.due_months_after_birth)
    

    def __str__(self):
        return f"{self.child.person.fullname} - {self.vaccine.name}"

