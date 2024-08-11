from django.test import TestCase
from .models import User, Sex, Role
from datetime import date

class UserModelTests(TestCase):

    def setUp(self):
        # Vytvoření několika uživatelů pro testy
        self.user1 = User.objects.create(
            name="Jakub",
            surname="Jakub",
            email="jakub@example.com",
            birth_date=date(1990, 1, 1),
            birth_number="123456",
            insurance=123456,
            gender=Sex.MAN,
            role_patient=Role.PATIENT,
            address="123 Ulica",
            contact="123-456-7890"
        )

        self.user2 = User.objects.create(
            name="Jana",
            surname="Jana",
            email="jana@example.com",
            birth_date=date(1990, 5, 5),
            birth_number="654321",
            insurance=654321,
            gender=Sex.WOMAN,
            role_patient=Role.DOCTOR,
            address="456 Ulica",
            contact="098-765-4321"
        )

    def test_create_user(self):
        user = User.objects.create(
            name="Tomáš",
            surname="Tomáš",
            email="tomas@example.com",
            birth_date=date(1990, 3, 3),
            birth_number="987654",
            insurance=987654,
            gender=Sex.NON_BINARY,
            role_patient=Role.NURSE,
            address="789 Ulica",
            contact="111-222-3333"
        )
        self.assertEqual(user.name, "Tomáš")
        self.assertEqual(user.surname, "Tomáš")
        self.assertEqual(user.email, "tomas@example.com")

    def test_unique_email(self):
        with self.assertRaises(Exception):
            User.objects.create(
                name="Jaroslav",
                surname="Jaroslav",
                email="jana@example.com",  # Tento email už existuje
                birth_date=date(1990, 4, 4),
                birth_number="456789",
                insurance=456789,
                gender=Sex.MAN,
                role_patient=Role.PATIENT,
                address="101 Ulica",
                contact="444-555-6666"
            )

    def test_user_str(self):
        user = User.objects.create(
            name="Pavel",
            surname="Novak",
            email="pavel@example.com",
            birth_date=date(1995, 6, 6),
            birth_number="123987",
            insurance=123987,
            gender=Sex.MAN,
            role_patient=Role.DOCTOR,
            address="789 Ulica",
            contact="777-888-9999"
        )
        self.assertEqual(str(user), "Pavel Novak : Doctor")

    def test_ordering(self):
        users = User.objects.all()
        self.assertEqual(users[0], self.user1)
        self.assertEqual(users[1], self.user2)

    def test_update_user(self):
        user = User.objects.get(email="jakub@example.com")
        user.name = "Updated Name"
        user.save()
        self.assertEqual(user.name, "Updated Name")
