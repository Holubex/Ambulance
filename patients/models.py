import locale

from django.db import models
from django.db.models import Model, TextChoices, IntegerChoices


# Definice výčtových tříd pro pohlaví, role a pojišťovny
class Sex(TextChoices):
    MAN = 'man', 'muž'
    WOMAN = 'woman', 'žena'
    NON_BINARY = 'non-binary', 'nebinární'


class Role(TextChoices):
    PATIENT = 'Patient', 'pacient'
    DOCTOR = 'Doctor', 'doktor'
    NURSE = 'Nurse', 'zdravotní sestra'


class InsuranceChoices(IntegerChoices):
    TYPE1 = 1, 'Všeobecná zdravotní pojišťovna (111)'  # Typ pojišťovny 1 s kódem a popisem
    TYPE2 = 2, 'Vojenská zdravotní pojišťovna ČR (201)'
    TYPE3 = 3, 'Česká průmyslová zdravotní pojišťovna (205)'
    TYPE4 = 4, 'Oborová zdravotní poj. zam. bank, poj. a stav. (207)'
    TYPE5 = 5, 'Zdravotní pojišťovna ministerstva vnitra ČR (211)'
    TYPE6 = 6, 'Revírní bratrská pokladna, zdrav. pojišťovna (213)'
    TYPE7 = 7, 'Zaměstnanecká pojišťovna Škoda (209)'


class User(Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    birth_number = models.CharField(max_length=20)
    insurance = models.PositiveSmallIntegerField(
        choices=InsuranceChoices.choices,
        default=InsuranceChoices.TYPE1
    )
    gender = models.CharField(max_length=10, choices=Sex.choices)
    role_patient = models.TextField(choices=Role.choices)
    address = models.TextField()
    contact = models.TextField()

    class Meta:
        ordering = ['surname', 'name']  # Uspořádat primárně podle příjmení a pak jména

    def __str__(self):
        return f'{self.surname} {self.name}'

    @staticmethod
    def get_sorted_users():
        locale.setlocale(locale.LC_COLLATE, 'cs_CZ.UTF-8')  # Nastavení českého locale pro správné třídění
        users = User.objects.all()  # Načtení všech uživatelů
        return sorted(users, key=lambda user: locale.strxfrm(user.surname))  # Třídění uživatelů podle příjmení
