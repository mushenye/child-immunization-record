# Generated by Django 5.0.4 on 2024-11-22 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateField(auto_now_add=True)),
                ("first_name", models.CharField(blank=True, max_length=50, null=True)),
                ("middle_name", models.CharField(blank=True, max_length=50, null=True)),
                ("last_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Vaccine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "due_months_after_birth",
                    models.IntegerField(
                        help_text="Months after birth when this vaccine is due."
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Caregiver",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="immunization_api.person",
                    ),
                ),
                ("email_address", models.EmailField(max_length=254)),
                ("parent_phone_number", models.CharField(max_length=15)),
                (
                    "parent",
                    models.CharField(
                        choices=[
                            ("Father", "Father"),
                            ("Mother", "Mother"),
                            ("Guardian", "Guardian"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
            bases=("immunization_api.person",),
        ),
        migrations.CreateModel(
            name="Child",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="immunization_api.person",
                    ),
                ),
                ("birth_date", models.DateField()),
                ("birth_weight", models.IntegerField()),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="immunization_api.caregiver",
                    ),
                ),
            ],
            bases=("immunization_api.person",),
        ),
        migrations.CreateModel(
            name="ImmunizationSchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateField(auto_now_add=True)),
                ("child_weight", models.IntegerField()),
                ("alert_sent", models.BooleanField(default=False, null=True)),
                (
                    "vaccine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="immunization_api.vaccine",
                    ),
                ),
                (
                    "child",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="immunization_api.child",
                    ),
                ),
            ],
        ),
    ]
