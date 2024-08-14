from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile

from django.urls import reverse

from accounts.views import RegistrationForm


# class ProfileModelTest(TestCase):
#     def test_profile_creation(self):
#         # Vytvoř uživatele
#         user = User.objects.create_user(username='testuser', password='12345')
#         # Automaticky by měl být vytvořen i profil
#         profile = Profile.objects.get(user=user)
#         # Ověření, že profil je správně propojen s uživatelem
#         self.assertEqual(profile.user, user)

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
        self.assertEqual(user.email, 'newuser@example.com')
        self.assertEqual(profile.birth_date.strftime('%Y-%m-%d'), '1990-01-01')

# Create your tests here.
