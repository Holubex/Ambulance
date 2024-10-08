# Generated by Django 4.1.1 on 2024-08-04 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=120)),
                ("surname", models.CharField(blank=True, max_length=120)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("birth_date", models.DateField()),
                ("birth_number", models.CharField(blank=True, max_length=20)),
                ("insurance", models.IntegerField()),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("man", "Man"),
                            ("woman", "Woman"),
                            ("non-binary", "Non Binary"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "role_patient",
                    models.TextField(
                        choices=[
                            ("Doctor", "Doctor"),
                            ("Nurse", "Nurse"),
                            ("Patient", "Patient"),
                        ]
                    ),
                ),
                ("address", models.TextField()),
                ("contact", models.TextField()),
            ],
            options={
                "ordering": ["birth_date"],
            },
        ),
    ]
