from django import forms
from .models import Appointment
from patients.models import User as Patient  # Importuje model User jako Patient

class AppointmentForm(forms.ModelForm):
    # Pole pro výběr doktora, pouze uživatelé s rolí 'Doctor'
    doctor = forms.ModelChoiceField(
        queryset=Patient.objects.filter(role_patient="Doctor"),  # Filtruje doktory
        label="Doktor",  # Popis pole
        widget=forms.Select,  # Typ widgetu (výběr z rozevíracího seznamu)
        required=True,  # Pole je povinné
    )

    # Pole pro výběr pacienta, zahrnuje všechny uživatele
    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),  # Načítá všechny uživatele jako pacienty
        label="Pacient",  # Popis pole
        widget=forms.Select,  # Typ widgetu (výběr z rozevíracího seznamu)
        required=True,  # Pole je povinné
    )

    class Meta:
        model = Appointment  # Určuje, že formulář je založen na modelu Appointment
        fields = ["doctor", "patient", "service", "day", "time"]  # Vybraná pole pro formulář
        labels = {
            "doctor": "Doktor",
            "service": "Důvod objednání",
            "day": "Den",
            "time": "Čas",
            "patient": "Pacient",
        }
        widgets = {
            "day": forms.DateInput(attrs={"type": "date"}),  # Widget pro výběr data
        }
