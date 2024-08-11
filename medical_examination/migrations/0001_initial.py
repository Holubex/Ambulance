# Generated by Django 4.1.1 on 2024-08-11 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("patients", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Announcement",
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
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="MedicalExamination",
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
                ("current_complaints", models.TextField(blank=True, null=True)),
                ("objective_findings", models.TextField(blank=True, null=True)),
                ("diagnosis", models.TextField(blank=True, null=True)),
                ("examination_date", models.DateField(auto_now_add=True)),
                ("prescription", models.TextField(blank=True, null=True)),
                (
                    "doctor",
                    models.ForeignKey(
                        limit_choices_to={"role_patient": "Doctor"},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="medical_examinations_as_doctor",
                        to="patients.patients",
                    ),
                ),
                (
                    "nurse",
                    models.ForeignKey(
                        limit_choices_to={"role_patient": "Nurse"},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="medical_examinations_as_nurse",
                        to="patients.patients",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        limit_choices_to={"role_patient": "Patient"},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="medical_examinations_as_patient",
                        to="patients.patients",
                    ),
                ),
            ],
            options={
                "ordering": ["examination_date"],
            },
        ),
    ]
