from django.db import models
from django.db.models import Model, TextChoices


# Create your models here.
class Sex(TextChoices):
    MAN = 'man', 'muž'
    WOMAN = 'woman', 'žena'
    NON_BINARY = 'non-binary', 'nebinární'


class Role(TextChoices):
    DOCTOR = 'Doctor', 'doktor'
    NURSE = 'Nurse', 'zdravotní sestra'
    PATIENT = 'Patient', 'pacient'


class User(Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120, blank=True)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    birth_number = models.CharField(max_length=20, blank=True)
    insurance = models.IntegerField()
    gender = models.CharField(max_length=10, choices=Sex.choices)
    role_patient = models.TextField(choices=Role.choices)
    address = models.TextField()
    contact = models.TextField()

    class Meta:
        ordering = ['birth_date']

    def __str__(self):
        return f'{self.name} {self.surname} : {self.role_patient}'
