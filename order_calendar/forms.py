from django import forms
from django.contrib.auth.models import User, Group
from .models import Appointment
from patients.models import User as Patient


class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(
        queryset=Patient.objects.filter(role_patient="Doctor"),
        label="Doktor",
        widget=forms.Select,
        required=True
    )

    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        label="Pacient",
        widget=forms.Select,
        required=True
    )

    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'service', 'day', 'time']
        labels = {
            'doctor': 'Doktor',
            'service': 'Důvod objednání',
            'day': 'Den',
            'time': 'Čas',
            'patient': 'Pacient',
        }
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date'}),
        }
