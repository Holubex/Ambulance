from django.db import models
from django.db.models import Model, CASCADE, ForeignKey, TextField, DateField

from users.models import User


class MedicalExamination(Model):
    # id = AutoField(primary_key=True)
    patient = ForeignKey(User, limit_choices_to={'role': 'Patient'}, on_delete=CASCADE,
                         related_name='medical_examinations_as_patient')
    nurse = ForeignKey(User, limit_choices_to={'role': 'Nurse'}, on_delete=CASCADE,
                       related_name='medical_examinations_as_nurse')
    doctor = ForeignKey(User, limit_choices_to={'role': 'Doctor'}, on_delete=CASCADE,
                        related_name='medical_examinations_as_doctor')
    current_complaints = TextField(blank=True, null=True)
    objective_findings = TextField(blank=True, null=True)
    diagnosis = TextField(blank=True, null=True)
    examination_date = DateField(auto_now_add=True)
    prescription = TextField(blank=True, null=True)

    class Meta:
        ordering = ['examination_date']
        permissions = [
            ("add_medical_examination", "Can add medical examination"),
        ]

    def __str__(self):
        return f"Pacient {self.patient} byl vyšetřen lékařem {self.doctor} dne {self.examination_date}."

# narozen {self.User.birth_date}
