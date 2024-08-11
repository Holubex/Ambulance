from django.db import models
from django.db.models import Model, CASCADE, ForeignKey, TextField, DateField

from patients.models import Patients


class MedicalExamination(Model):
    # id = AutoField(primary_key=True)
    patient = ForeignKey(
        Patients,
        limit_choices_to={"role_patient": "Patient"},
        on_delete=CASCADE,
        related_name="medical_examinations_as_patient",
    )
    nurse = ForeignKey(
        Patients,
        limit_choices_to={"role_patient": "Nurse"},
        on_delete=CASCADE,
        related_name="medical_examinations_as_nurse",
    )
    doctor = ForeignKey(
        Patients,
        limit_choices_to={"role_patient": "Doctor"},
        on_delete=CASCADE,
        related_name="medical_examinations_as_doctor",
    )
    current_complaints = TextField(blank=True, null=True)
    objective_findings = TextField(blank=True, null=True)
    diagnosis = TextField(blank=True, null=True)
    examination_date = DateField(auto_now_add=True)
    prescription = TextField(blank=True, null=True)

    class Meta:
        ordering = ["examination_date"]

    def __str__(self):
        return f"Pacient {self.patient} byl vyšetřen lékařem {self.doctor} dne {self.examination_date}."


class Announcement(Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
