from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile

from django.urls import reverse

from accounts.views import RegistrationForm


class ProfileModelTest(TestCase):
    def setUp(self):
        # Vytvoření instance uživatele pro testování
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_profile_creation(self):
        # Vytvoření profilu spojeného s vytvořeným uživatelem
        profile = Profile.objects.create(user=self.user, birth_date='1990-01-01')

        # Kontrola, zda byl profil úspěšně vytvořen
        self.assertIsInstance(profile, Profile)
        self.assertEqual(profile.user.username, 'testuser')
        self.assertEqual(profile.birth_date, '1990-01-01')

    def test_profile_str_representation(self):
        # Vytvoření profilu spojeného s vytvořeným uživatelem
        profile = Profile.objects.create(user=self.user, birth_date='1990-01-01')

        # Kontrola textové reprezentace profilu
        self.assertEqual(str(profile), 'testuser')

class RegistrationFormTest(TestCase):
    def test_registration_form(self):
        form_data = {
            'username': 'newuser',
            'password1': 'complex_password123',
            'password2': 'complex_password123',
            'email': 'test@gmail.com',
            'birth_date': '1990-01-01'
        }
        form = RegistrationForm(data=form_data)
        # Ověření, že formulář je validní
        self.assertTrue(form.is_valid())
        # Uložení uživatele
        user = form.save()
        # Ověření, že uživatel byl vytvořen
        self.assertEqual(User.objects.count(), 1)
        # Ověření, že profil byl vytvořen
        self.assertEqual(Profile.objects.count(), 1)
        # Ověření, že email a datum narození jsou správně uloženy
        profile = Profile.objects.get(user=user)
        self.assertEqual(user.email, 'test@gmail.com')
        self.assertEqual(profile.birth_date.strftime('%Y-%m-%d'), '1990-01-01')

# Create your tests here.
