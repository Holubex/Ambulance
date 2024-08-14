from django.db import models
from datetime import datetime, date
from patients.models import User as Patient  # Importuje model User jako Patient

# Definice možných služeb
SERVICE_CHOICES = (
    ("Vstupní vyšetření", "Vstupní vyšetření"),
    ("Kontrola", "Kontrola"),
    ("Recept", "Recept"),
    ("Potvrzení, výpis", "Potvrzení, výpis"),
    ("Jiný důvod", "Jiný důvod"),
)

# Definice možných časů
TIME_CHOICES = (
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
)

class Appointment(models.Model):
    # Doktor je cizí klíč na model Patient, může být prázdný
    doctor = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,  # Při smazání doktora se smažou i jeho schůzky
        null=True,
        blank=True,
        related_name="appointments_as_doctor",  # Vztah pro získání všech schůzek tohoto doktora
    )
    # Služba - výběr z předdefinovaných možností
    service = models.CharField(
        max_length=50, choices=SERVICE_CHOICES, default="Doctor care"
    )
    # Pacient je cizí klíč na model Patient, může být prázdný
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=True, blank=True, related_name="patient"
    )
    # Datum schůzky, výchozí hodnota je aktuální datum
    day = models.DateField(default=datetime.now)
    # Čas schůzky - výběr z předdefinovaných možností
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    # Datum a čas vytvoření schůzky
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ["day"]  # Řadí schůzky podle data

    def save(self, *args, **kwargs):
        self.delete_past_appointments()  # Před uložením smaže minulá data
        super(Appointment, self).save(*args, **kwargs)  # Uloží aktuální schůzku

    @staticmethod
    def delete_past_appointments():
        # Vymaže všechny schůzky s datem v minulosti
        Appointment.objects.filter(day__lt=date.today()).delete()

    def __str__(self):
        # Vypíše základní informace o schůzce
        return f"{self.patient.username} | Doktor: {self.doctor.username} | den: {self.day} | čas: {self.time}"
