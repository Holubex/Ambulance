from django.forms import ModelForm

from medical_examination.models import MedicalExamination, Announcement


class MedicalExaminationForm(ModelForm):
    class Meta:
        model = MedicalExamination  # Specifikuje model, se kterým bude formulář pracovat
        fields = '__all__'  # Zahrne všechna pole z modelu do formuláře
        labels = {
            'patient': 'Pacient',  # Nastavuje český štítek pro pole 'patient'
            'nurse': 'Zdravotní sestra',
            'doctor': 'Doktor',
            'current_complaints': 'Aktuální obtíže',
            'objective_findings': 'Objektivní nález',
            'diagnosis': 'Diagnóza',
            'prescription': 'Recept',
        }


class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement  # Specifikuje model, se kterým bude formulář pracovat
        fields = ['title', 'content']  # Zahrne pouze pole 'title' a 'content' do formuláře
        labels = {
            'title': 'Nadpis',  # Nastavuje český štítek pro pole 'title'
            'content': 'Obsah',
        }
