from django.db import models
from django.db.models import Model, CASCADE, ForeignKey, TextField, DateField

from patients.models import User


class MedicalExamination(Model):
    # id = AutoField(primary_key=True)  # Automaticky generované primární klíčové pole
    patient = ForeignKey(
        User,
        limit_choices_to={"role_patient": "Patient"},  # Omezuje výběr na uživatele s rolí 'Patient'
        on_delete=CASCADE,  # Při smazání uživatele smaže i všechny jeho vyšetření
        related_name="medical_examinations_as_patient",  # Vytváří zpětný vztah pro přístup k vyšetřením z uživatele
    )
    nurse = ForeignKey(
        User,
        limit_choices_to={"role_patient": "Nurse"},  # Omezuje výběr na uživatele s rolí 'Nurse'
        on_delete=CASCADE,
        related_name="medical_examinations_as_nurse",
    )
    doctor = ForeignKey(
        User,
        limit_choices_to={"role_patient": "Doctor"},  # Omezuje výběr na uživatele s rolí 'Doctor'
        on_delete=CASCADE,
        related_name="medical_examinations_as_doctor",
    )
    current_complaints = TextField(blank=True, null=True)  # Textové pole pro aktuální obtíže, může být prázdné
    objective_findings = TextField(blank=True, null=True)
    diagnosis = TextField(blank=True, null=True)
    examination_date = DateField(auto_now_add=True)  # Automaticky nastaví datum vyšetření na aktuální datum
    prescription = TextField(blank=True, null=True)

    class Meta:
        ordering = ["examination_date"]  # Řazení vyšetření podle data

    def __str__(self):
        return f"Pacient {self.patient} byl vyšetřen lékařem {self.doctor} dne {self.examination_date}."


class Announcement(Model):
    title = models.CharField(max_length=200)  # Pole pro název oznámení, omezené na 200 znaků
    content = models.TextField()  # Pole pro obsah oznámení
    created_at = models.DateTimeField(auto_now_add=True)  # Automaticky nastaví datum vytvoření oznámení

    class Meta:
        ordering = ["-created_at"]  # Řazení oznámení podle data vytvoření, od nejnovějšího

    def __str__(self):
        return self.title
