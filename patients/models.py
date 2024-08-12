from django.db import models
from django.db.models import Model, TextChoices, IntegerChoices


# Create your models here.
class Sex(TextChoices):
    MAN = 'man', 'muž'
    WOMAN = 'woman', 'žena'
    NON_BINARY = 'non-binary', 'nebinární'


class Role(TextChoices):
    DOCTOR = 'Doctor', 'doktor'
    NURSE = 'Nurse', 'zdravotní sestra'
    PATIENT = 'Patient', 'pacient'


class InsuranceChoices(IntegerChoices):
    TYPE1 = 1, 'Všeobecná zdravotní pojišťovna (111)'
    TYPE2 = 2, 'Vojenská zdravotní pojišťovna ČR (201)'
    TYPE3 = 3, 'Česká průmyslová zdravotní pojišťovna (205)'
    TYPE4 = 4, 'Oborová zdravotní poj. zam. bank, poj. a stav. (207)'
    TYPE5 = 5, 'Zdravotní pojišťovna ministerstva vnitra ČR (211)'
    TYPE6 = 6, 'Revírní bratrská pokladna, zdrav. pojišťovna (213)'
    TYPE7 = 7, 'Zaměstnanecká pojišťovna Škoda (209)'


class User(Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120, blank=True)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    birth_number = models.CharField(max_length=20, blank=True)
    insurance = models.PositiveSmallIntegerField(
        choices=InsuranceChoices.choices,
        default=InsuranceChoices.TYPE1
    )
    gender = models.CharField(max_length=10, choices=Sex.choices)
    role_patient = models.TextField(choices=Role.choices)
    address = models.TextField()
    contact = models.TextField()

    class Meta:
        ordering = ['birth_date']

    def __str__(self):
        return f'{self.name} {self.surname}'
        # return f'{self.name} {self.surname} : {self.role_patient}'
