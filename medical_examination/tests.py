from django.test import TestCase
from datetime import date
from patients.models import User
from .models import MedicalExamination, Announcement

class MedicalExaminationModelTests(TestCase):

    def setUp(self):
        # Vytvoření uživatelů (pacient, sestra, doktor) pro testy
        self.patient = User.objects.create(
            name="Jan",
            surname="Janovsky",
            email="jan@email.com",
            birth_date=date(1990, 1, 1),
            birth_number="123456",
            insurance=123456,
            gender='man',
            role_patient='Patient',
            address="Ulica 123",
            contact="123-456-7890"
        )

        self.nurse = User.objects.create(
            name="Pavla",
            surname="Pavlovska",
            email="pavla@email.com",
            birth_date=date(1985, 5, 5),
            birth_number="654321",
            insurance=654321,
            gender='woman',
            role_patient='Nurse',
            address="Ulica 456",
            contact="098-765-4321"
        )

        self.doctor = User.objects.create(
            name="MUDr. Tomáš",
            surname="Doktorovský",
            email="tomas@email.com",
            birth_date=date(1980, 10, 10),
            birth_number="789456",
            insurance=789456,
            gender='man',
            role_patient='Doctor',
            address="Ulica 789",
            contact="111-222-3333"
        )

    def test_create_medical_examination(self):
        # Test vytvoření nového lékařského vyšetření
        medical_examination = MedicalExamination.objects.create(
            patient=self.patient,
            nurse=self.nurse,
            doctor=self.doctor,
            current_complaints="Priznaky",
            objective_findings="Nález",
            diagnosis="Diagnoza",
            prescription="Liek 1 - 2x do dne, Liek 2 - 1x do dne",
        )
        self.assertEqual(medical_examination.patient, self.patient)
        self.assertEqual(medical_examination.nurse, self.nurse)
        self.assertEqual(medical_examination.doctor, self.doctor)
        self.assertEqual(medical_examination.current_complaints, "Priznaky")
        self.assertEqual(medical_examination.diagnosis, "Diagnoza")

    def test_ordering_medical_examinations(self):
        # Test řazení lékařských vyšetření podle data vyšetření
        exam1 = MedicalExamination.objects.create(
            patient=self.patient,
            nurse=self.nurse,
            doctor=self.doctor,
            examination_date=date(2024, 1, 1)
        )
        exam2 = MedicalExamination.objects.create(
            patient=self.patient,
            nurse=self.nurse,
            doctor=self.doctor,
            examination_date=date(2024, 2, 1)
        )
        examinations = MedicalExamination.objects.all()
        self.assertEqual(examinations[0], exam1)
        self.assertEqual(examinations[1], exam2)


class AnnouncementModelTests(TestCase):

    def test_create_announcement(self):
        # Test vytvoření nového oznámení
        announcement = Announcement.objects.create(
            title="Nové vyšetření",
            content="Bylo zavedeno nové lékařské vyšetření."
        )
        self.assertEqual(announcement.title, "Nové vyšetření")
        self.assertEqual(announcement.content, "Bylo zavedeno nové lékařské vyšetření.")

    def test_ordering_announcements(self):
        # Test řazení oznámení podle data vytvoření
        ann1 = Announcement.objects.create(
            title="První oznámení",
            content="Obsah prvního oznámení.",
            created_at=date(2024, 1, 1)
        )
        ann2 = Announcement.objects.create(
            title="Druhé oznámení",
            content="Obsah druhého oznámení.",
            created_at=date(2024, 2, 1)
        )
        announcements = Announcement.objects.all()
        self.assertEqual(announcements[0], ann2)
        self.assertEqual(announcements[1], ann1)
