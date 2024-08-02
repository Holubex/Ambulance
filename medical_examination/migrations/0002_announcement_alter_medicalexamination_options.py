# Generated by Django 4.1.1 on 2024-07-27 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medical_examination", "0001_initial"),
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
        migrations.AlterModelOptions(
            name="medicalexamination",
            options={"ordering": ["examination_date"]},
        ),
    ]
