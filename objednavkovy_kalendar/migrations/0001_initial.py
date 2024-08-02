# Generated by Django 4.1.1 on 2024-07-28 12:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0005_rename_role_user_role_patient"),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
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
                (
                    "service",
                    models.CharField(
                        choices=[
                            ("Vstupní vyšetření", "Vstupní vyšetření"),
                            ("Kontrola", "Kontrola"),
                            ("Recept", "Recept"),
                            ("potvrzení, výpis", "potvrzení, výpis"),
                            ("jiný důvod", "jiný důvod"),
                        ],
                        default="Doctor care",
                        max_length=50,
                    ),
                ),
                ("day", models.DateField(default=datetime.datetime.now)),
                (
                    "time",
                    models.CharField(
                        choices=[
                            ("08:00", "08:00"),
                            ("08:30", "08:30"),
                            ("09:00", "09:00"),
                            ("09:30", "09:30"),
                            ("10:00", "10:00"),
                            ("10:30", "10:30"),
                            ("11:00", "11:00"),
                            ("11:30", "11:30"),
                            ("12:00", "12:00"),
                            ("12:30", "12:30"),
                            ("13:00", "13:00"),
                            ("13:30", "13:30"),
                            ("14:00", "14:00"),
                            ("14:30", "14:30"),
                            ("15:00", "15:00"),
                            ("15:30", "15:30"),
                            ("16:00", "16:00"),
                            ("16:30", "16:30"),
                            ("17:00", "17:00"),
                            ("17:30", "17:30"),
                            ("18:00", "18:00"),
                        ],
                        default="3 PM",
                        max_length=10,
                    ),
                ),
                (
                    "time_ordered",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
                (
                    "doctor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="appointments_as_doctor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient",
                        to="users.user",
                    ),
                ),
            ],
        ),
    ]
