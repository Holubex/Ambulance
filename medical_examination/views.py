# views.py
from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from medical_examination.forms import MedicalExaminationForm, AnnouncementForm
from medical_examination.models import MedicalExamination, Announcement
from patients.models import User as Patient, Role


# Formulář pro filtrování lékařských vyšetření
class MedicalExaminationFilterForm(forms.Form):
    patient = forms.ModelChoiceField(
        # Výběr pacientů s rolí 'PATIENT', seřazeno podle příjmení a jména
        queryset=Patient.objects.filter(role_patient=Role.PATIENT).order_by('surname', 'name'),
        required=False,  # Toto pole není povinné
        label='Pacient',  # Popis pole, který bude zobrazen v šabloně
        widget=forms.Select(attrs={'class': 'form-control'})  # Používá CSS třídu 'form-control' pro stylování
    )
    nurse = forms.ModelChoiceField(
        # Výběr sestřiček s rolí 'NURSE', seřazeno podle příjmení a jména
        queryset=Patient.objects.filter(role_patient=Role.NURSE).order_by('surname', 'name'),
        required=False,  # Toto pole není povinné
        label='Sestřička',  # Popis pole, který bude zobrazen v šabloně
        widget=forms.Select(attrs={'class': 'form-control'})  # Používá CSS třídu 'form-control' pro stylování
    )
    doctor = forms.ModelChoiceField(
        # Výběr lékařů s rolí 'DOCTOR', seřazeno podle příjmení a jména
        queryset=Patient.objects.filter(role_patient=Role.DOCTOR).order_by('surname', 'name'),
        required=False,  # Toto pole není povinné
        label='Lékař',  # Popis pole, který bude zobrazen v šabloně
        widget=forms.Select(attrs={'class': 'form-control'})  # Používá CSS třídu 'form-control' pro stylování
    )
    examination_date = forms.DateField(
        # Výběr data vyšetření
        required=False,  # Toto pole není povinné
        label='Datum vyšetření',  # Popis pole, který bude zobrazen v šabloně
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'})  # Používá textové pole s typem 'date' pro výběr data
    )

    def filter(self, queryset):
        # Filtruje queryset na základě vyplněných polí formuláře
        if self.is_valid():
            data = self.cleaned_data
            if data.get('patient'):
                queryset = queryset.filter(patient_id=data['patient'].id)  # Filtruje podle ID pacienta
            if data.get('nurse'):
                queryset = queryset.filter(nurse_id=data['nurse'].id)  # Filtruje podle ID sestřičky
            if data.get('doctor'):
                queryset = queryset.filter(doctor_id=data['doctor'].id)  # Filtruje podle ID lékaře
            if data.get('examination_date'):
                queryset = queryset.filter(examination_date=data['examination_date'])  # Filtruje podle data vyšetření
        return queryset


# Zobrazení seznamu lékařských vyšetření s možností filtrování
class MedicalExaminationListView(ListView):
    model = MedicalExamination
    template_name = "medical_examination_list.html"
    context_object_name = "examinations"

    def get_context_data(self, **kwargs):
        # Přidává do kontextu seznam sestřiček a lékařů a formulář pro filtrování
        context = super().get_context_data(**kwargs)
        context['nurses'] = Patient.objects.filter(role_patient=Role.NURSE)
        context['doctors'] = Patient.objects.filter(role_patient=Role.DOCTOR)
        context['filter_form'] = MedicalExaminationFilterForm(self.request.GET)
        return context

    def get_queryset(self):
        # Získá queryset lékařských vyšetření a aplikuje filtry na základě dotazu
        queryset = super().get_queryset().select_related('patient', 'nurse', 'doctor')
        patient_name = self.request.GET.get('patient_name', '')  # Získá jméno pacienta z GET parametrů
        nurse_id = self.request.GET.get('nurse_id', '')  # Získá ID sestřičky z GET parametrů
        doctor_id = self.request.GET.get('doctor_id', '')  # Získá ID lékaře z GET parametrů

        # Pokud je zadáno jméno pacienta, filtruje podle příjmení nebo jména pacienta
        if patient_name:
            queryset = queryset.filter(
                Q(patient__surname__icontains=patient_name) |
                Q(patient__name__icontains=patient_name)
            )
        # Pokud je zadáno ID sestřičky, filtruje podle ID sestřičky
        if nurse_id:
            queryset = queryset.filter(nurse_id=nurse_id)
        # Pokud je zadáno ID lékaře, filtruje podle ID lékaře
        if doctor_id:
            queryset = queryset.filter(doctor_id=doctor_id)

        # Seřadí výsledky podle příjmení a jména pacienta, sestřičky a lékaře
        return queryset.order_by(
            'patient__surname', 'patient__name',
            'nurse__surname', 'nurse__name',
            'doctor__surname', 'doctor__name'
        )


# Zobrazení pro vytvoření nového lékařského vyšetření
class MedicalExaminationCreateView(CreateView):
    template_name = 'medical_examination_form.html'
    form_class = MedicalExaminationForm
    success_url = reverse_lazy('medical_examination_list')
    permission_required = 'medical_examination.add_medical_examination'


# Zobrazení detailu lékařského vyšetření
class MedicalExaminationDetailView(DetailView):
    template_name = 'medical_examination_detail.html'
    model = MedicalExamination
    context_object_name = 'medical_examination'


# Zobrazení pro aktualizaci lékařského vyšetření
class MedicalExaminationUpdateView(UpdateView):
    template_name = 'medical_examination_form.html'
    form_class = MedicalExaminationForm
    model = MedicalExamination
    success_url = reverse_lazy('medical_examination_list')
    permission_required = 'medical_examination.change_medical_examination'

    def get_context_data(self, **kwargs):
        # Přidá do kontextu název akce pro formulář
        context = super().get_context_data(**kwargs)
        context['form_action'] = 'Upravit vyšetření'
        return context


# Zobrazení pro smazání lékařského vyšetření
class MedicalExaminationDeleteView(DeleteView):
    template_name = 'medical_examination_confirm_delete.html'
    model = MedicalExamination
    success_url = reverse_lazy('medical_examination_list')
    permission_required = 'medical_examination.delete_medical_examination'

    def get_context_data(self, **kwargs):
        # Přidá do kontextu název akce pro potvrzení smazání
        context = super().get_context_data(**kwargs)
        context['form_action'] = 'Vymazat vyšetření'
        return context


# Zobrazení seznamu oznámení
class AnnouncementListView(ListView):
    template_name = 'announcement_list.html'
    model = Announcement
    context_object_name = 'announcements'


# Zobrazení pro vytvoření nového oznámení
class AnnouncementCreateView(CreateView):
    template_name = 'announcement_form.html'
    form_class = AnnouncementForm
    success_url = reverse_lazy('announcement_list')


# Zobrazení pro aktualizaci oznámení
class AnnouncementUpdateView(UpdateView):
    template_name = 'announcement_form.html'
    form_class = AnnouncementForm
    model = Announcement
    success_url = reverse_lazy('announcement_list')


# Zobrazení pro smazání oznámení
class AnnouncementDeleteView(DeleteView):
    template_name = 'announcement_confirm_delete.html'
    model = Announcement
    success_url = reverse_lazy('announcement_list')
