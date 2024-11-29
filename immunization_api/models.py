
from django.db import models
from dateutil.relativedelta import relativedelta
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from PIL import Image  
import uuid  


class Person(models.Model):
    date_created = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def get_slug_string(self):
        elements = [self.first_name, self.middle_name, self.last_name]
        filtered_elements = filter(None, elements)
        return ' '.join(filtered_elements)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.get_slug_string())
            self.slug = base_slug
            while Person.objects.filter(slug=self.slug).exists():
                self.slug = f'{base_slug}-{uuid.uuid4().hex[:6]}'

        super().save(*args, **kwargs)

        if self.profile_picture:
            img = Image.open(self.profile_picture.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_picture.path)

    @property
    def fullname(self):
        name_parts = [self.first_name.capitalize(), self.middle_name.capitalize(), self.last_name.capitalize()]
        return " ".join(filter(None, name_parts))

    def clean(self):
        super().clean()
        if not self.last_name.strip():
            raise ValidationError("Last name cannot be blank or whitespace.")

    def __str__(self):
        return self.fullname



class Caregiver(Person):
    email_address = models.EmailField()
    parent_phone_number = models.CharField(max_length=15)
    parent = models.CharField(
        choices=[
            ('Father', 'Father'),
            ('Mother', 'Mother'),
            ('Guardian', 'Guardian')
        ],
        max_length=50
    )
    occupation = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.fullname

class Child(Person):
    parent =models.ForeignKey(Caregiver, on_delete=models.CASCADE)
    birth_date = models.DateField()
    birth_weight=models.IntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True, null=True)

    

    def __str__(self):
        return self.fullname   
    

class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_months_after_birth = models.IntegerField(help_text="Months after birth when this vaccine is due.")

    def __str__(self):
        return self.name

class ImmunizationSchedule(models.Model):
    date_created=models.DateField(auto_now_add=True)
    child_weight=models.DecimalField(max_digits=4, decimal_places=2)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    alert_sent = models.BooleanField(default=False, null=True)

    @property
    def due_date(self):
        return self.child.birth_date + relativedelta(months=self.vaccine.due_months_after_birth)
    

    def __str__(self):
        return f"{self.child.fullname} - {self.vaccine.name}"

