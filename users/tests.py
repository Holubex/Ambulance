from django.test import TestCase
from .models import User, Sex, Role
from datetime import date

class UserModelTests(TestCase):

    def setUp(self):
        # Vytvoření několika uživatelů pro testy
        self.user1 = User.objects.create(
            name="John",
            surname="Doe",
            email="john@example.com",
            birth_date=date(1990, 1, 1),
            birth_number="123456",
            insurance=123456,
            gender=Sex.MAN,
            role_patient=Role.PATIENT,
            address="123 Main St",
            contact="123-456-7890"
        )

        self.user2 = User.objects.create(
            name="Jane",
            surname="Doe",
            email="jane@example.com",
            birth_date=date(1985, 5, 5),
            birth_number="654321",
            insurance=654321,
            gender=Sex.WOMAN,
            role_patient=Role.DOCTOR,
            address="456 Main St",
            contact="098-765-4321"
        )

    def test_create_user(self):
        user = User.objects.create(
            name="Alice",
            surname="Smith",
            email="alice@example.com",
            birth_date=date(1995, 3, 3),
            birth_number="987654",
            insurance=987654,
            gender=Sex.NON_BINARY,
            role_patient=Role.NURSE,
            address="789 Main St",
            contact="111-222-3333"
        )
        self.assertEqual(user.name, "Alice")
        self.assertEqual(user.surname, "Smith")
        self.assertEqual(user.email, "alice@example.com")

    def test_unique_email(self):
        with self.assertRaises(Exception):
            User.objects.create(
                name="Bob",
                surname="Johnson",
                email="john@example.com",  # Tento email už existuje
                birth_date=date(1992, 4, 4),
                birth_number="456789",
                insurance=456789,
                gender=Sex.MAN,
                role_patient=Role.PATIENT,
                address="101 Main St",
                contact="444-555-6666"
            )

    def test_ordering_by_birth_date(self):
        users = User.objects.all()
        self.assertEqual(users[0], self.user2)  # Jane Doe (1985) by měla být první
        self.assertEqual(users[1], self.user1)  # John Doe (1990) by měl být druhý

    def test_string_representation(self):
        self.assertEqual(str(self.user1), "John Doe : Patient")
        self.assertEqual(str(self.user2), "Jane Doe : Doctor")

    def test_optional_fields(self):
        user = User.objects.create(
            name="Charlie",
            surname="Brown",
            email="charlie@example.com",
            birth_date=date(1980, 7, 7),
            insurance=123123,
            gender=Sex.MAN,
            role_patient=Role.PATIENT,
            address="987 Other St",
            contact="777-888-9999"
        )
        self.assertEqual(user.surname, "Brown")
        self.assertEqual(user.birth_number, "")
