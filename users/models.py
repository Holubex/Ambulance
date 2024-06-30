from django.db import models
from django.db.models import Model, TextChoices


# Create your models here.
class Sex(TextChoices):
    MAN = 'man'
    WOMAN = 'woman'
    NON_BINARY = 'non-binary'


class Role(TextChoices):
    DOCTOR = 'Doctor'
    NURSE = 'Nurse'
    PATIENT = 'Patient'

class User(Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120, blank=True)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    birth_number = models.CharField(max_length=20, blank=True)
    insurance = models.IntegerField()
    gender = role = models.CharField(max_length=10, choices=Sex.choices)
    role = models.TextField(choices=Role.choices)
    address = models.TextField()
    contact = models.TextField()

    class Meta:
        ordering = ['birth_date']

    def __str__(self):
        return f'{self.name} {self.surname} : {self.role}'