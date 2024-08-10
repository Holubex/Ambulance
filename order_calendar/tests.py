from django.test import TestCase
from .models import Appointment
from patients.models import User as Patient
from datetime import date, datetime

class AppointmentModelTests(TestCase):

    def setUp(self):
        # Vytvorenie pacienta a doktora pre testy
        self.patient = Patient.objects.create(
            name="John",
            surname="Doe",
            email="john@example.com",
            birth_date=date(1990, 1, 1),
            birth_number="123456",
            insurance=123456,
            gender='man',
            role_patient='Patient',
            address="123 Main St",
            contact="123-456-7890"
        )

        self.doctor = Patient.objects.create(
            name="Dr. Smith",
            surname="Smith",
            email="dr.smith@example.com",
            birth_date=date(1980, 2, 2),
            birth_number="654321",
            insurance=654321,
            gender='man',
            role_patient='Doctor',
            address="456 Oak St",
            contact="987-654-3210"
        )

    def test_create_appointment(self):
        # Tento test ověřuje, zda byl v modelu Appointment správně vytvořen nový záznam (schůzka).
        appointment = Appointment.objects.create(
            doctor=self.doctor,
            service="Kontrola",
            patient=self.patient,
            day=date(2024, 8, 10),
            time="10:00"
        )
        self.assertEqual(appointment.doctor, self.doctor)
        self.assertEqual(appointment.patient, self.patient)
        self.assertEqual(appointment.day, date(2024, 8, 10))
        self.assertEqual(appointment.time, "10:00")

    def test_delete_past_appointments(self):
        # Tento test ověřuje, zda jsou schůzky s datem v minulosti správně odstraněny.

        # Vytvořte záznam o schůzce s datem v minulosti.
        past_appointment = Appointment.objects.create(
            doctor=self.doctor,
            service="Kontrola",
            patient=self.patient,
            day=date(2023, 8, 1),
            time="10:00"
        )

        # Vytvorenie záznamu s dátumom v budúcnosti
        future_appointment = Appointment.objects.create(
            doctor=self.doctor,
            service="Kontrola",
            patient=self.patient,
            day=date(2024, 8, 10),
            time="10:00"
        )

        # Uloženie nového záznamu by malo vymazať záznam s dátumom 2023-08-01
        future_appointment.save()

        # Overenie, že záznam s dátumom v minulosti bol vymazaný
        self.assertFalse(Appointment.objects.filter(day=date(2023, 8, 1)).exists())

