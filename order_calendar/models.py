# Create your models here.
from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
from patients.models import User as Patient

# Definice možností pro službu (service) v podobě dvojic (hodnota, zobrazený text)
SERVICE_CHOICES = (
    ("Vstupní vyšetření", "Vstupní vyšetření"),
    ("Kontrola", "Kontrola"),
    ("Recept", "Recept"),
    ("Potvrzení, výpis", "Potvrzení, výpis"),
    ("Jiný důvod", "Jiný důvod"),
)

# Definice možností pro čas v podobě dvojic (hodnota, zobrazený text)
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


# Definice modelu Appointment (schůzky)
class Appointment(models.Model):
    doctor = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="appointments_as_doctor",
    )
    service = models.CharField(
        max_length=50, choices=SERVICE_CHOICES, default="Doctor care"
    )
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=True, blank=True, related_name="patient"
    )
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ["day"]

    def save(self, *args, **kwargs):
        self.delete_past_appointments()

    @staticmethod
    def delete_past_appointments():
        # Vymaže všetky záznamy s dátumom v minulosti
        Appointment.objects.filter(day__lt=date.today()).delete()


def __str__(self):
    return f"{self.user.username} | Doktor: {self.doctor.username} | den: {self.day} | čas: {self.time}"
