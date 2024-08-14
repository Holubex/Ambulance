from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from medical_examination.forms import MedicalExaminationForm, AnnouncementForm
from medical_examination.models import MedicalExamination, Announcement
from patients.models import User, Role


# Formulář pro filtrování lékařských vyšetření
class MedicalExaminationFilterForm(forms.Form):
    patient = forms.ModelChoiceField(
        queryset=User.objects.filter(role_patient=Role.PATIENT).order_by('surname', 'name'),  # Přizpůsobte filtrování
        required=False,  # Pole není povinné, uživatel jej nemusí vyplnit
        label='Pacient',
        widget=forms.Select(attrs={'class': 'form-control'})  # Stylování pomocí CSS třídy
    )
    nurse = forms.ModelChoiceField(
        queryset=User.objects.filter(role_patient=Role.NURSE).order_by('surname', 'name'),
        required=False,  # Pole není povinné
        label='Sestřička',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    doctor = forms.ModelChoiceField(
        queryset=User.objects.filter(role_patient=Role.DOCTOR).order_by('surname', 'name'),
        required=False,  # Pole není povinné
        label='Lékař',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    examination_date = forms.DateField(
        required=False,  # Pole není povinné
        label='Datum vyšetření',
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'})  # Textové pole pro výběr data
    )

    def filter(self, queryset):
        # Filtruje queryset na základě vyplněných polí formuláře
        if self.is_valid():
            data = self.cleaned_data  # Získá validovaná data z formuláře
            if data.get('patient'):
                queryset = queryset.filter(patient_id=data['patient'].id)  # Filtruje podle ID pacienta
            if data.get('nurse'):
                queryset = queryset.filter(nurse_id=data['nurse'].id)  # Filtruje podle ID sestřičky
            if data.get('doctor'):
                queryset = queryset.filter(doctor_id=data['doctor'].id)  # Filtruje podle ID lékaře
            if data.get('examination_date'):
                queryset = queryset.filter(examination_date=data['examination_date'])  # Filtruje podle data vyšetření
        return queryset


# Zobrazení seznamu lékařských vyšetření
class MedicalExaminationListView(ListView):
    template_name = 'medical_examination_list.html'
    model = MedicalExamination  # Model, ze kterého se načítají data
    context_object_name = 'examinations'  # Název objektu v šabloně
    permission_required = 'medical_examination.view_medical_examination'  # Požadované oprávnění

    def get_queryset(self):
        # Získá a filtruje queryset vyšetření na základě formuláře
        form = MedicalExaminationFilterForm(self.request.GET)
        queryset = super().get_queryset().select_related('patient', 'nurse', 'doctor')  # Efektivnější dotazy s relacemi

        if form.is_valid():
            queryset = form.filter(queryset)  # Aplikace filtrování na queryset

        queryset = queryset.order_by(
            'patient__surname', 'patient__name',
            'nurse__surname', 'nurse__name',
            'doctor__surname', 'doctor__name'
        )  # Seřazení podle příjmení a jména
        return queryset

    def get_context_data(self, **kwargs):
        # Přidá formulář pro filtrování do kontextu
        context = super().get_context_data(**kwargs)
        context['filter_form'] = MedicalExaminationFilterForm(self.request.GET)  # Formulář pro zobrazení
        return context


# Zobrazení pro vytvoření nového lékařského vyšetření
class MedicalExaminationCreateView(CreateView):
    template_name = 'medical_examination_form.html'
    form_class = MedicalExaminationForm  # Třída formuláře
    success_url = reverse_lazy('medical_examination_list')  # Přesměrování po úspěšném vytvoření
    permission_required = 'medical_examination.add_medical_examination'  # Požadované oprávnění


# Zobrazení detailu lékařského vyšetření
class MedicalExaminationDetailView(DetailView):
    template_name = 'medical_examination_detail.html'
    model = MedicalExamination  # Model, ze kterého se zobrazují detaily
    context_object_name = 'medical_examination'  # Název objektu v šabloně


# Zobrazení pro aktualizaci lékařského vyšetření
class MedicalExaminationUpdateView(UpdateView):
    template_name = 'medical_examination_form.html'
    form_class = MedicalExaminationForm  # Třída formuláře
    model = MedicalExamination  # Přidává model pro identifikaci vyšetření
    success_url = reverse_lazy('medical_examination_list')  # Přesměrování po úspěšné aktualizaci
    permission_required = 'medical_examination.change_medical_examination'  # Požadované oprávnění

    def get_context_data(self, **kwargs):
        # Přidá do kontextu název akce pro formulář
        context = super().get_context_data(**kwargs)
        context['form_action'] = 'Upraviť vyšetření'  # Popis akce ve formuláři
        return context


# Zobrazení pro smazání lékařského vyšetření
class MedicalExaminationDeleteView(DeleteView):
    template_name = 'medical_examination_confirm_delete.html'
    model = MedicalExamination  # Určuje model pro smazání
    success_url = reverse_lazy('medical_examination_list')  # Přesměrování po úspěšném smazání
    permission_required = 'medical_examination.delete_medical_examination'  # Požadované oprávnění

    def get_context_data(self, **kwargs):
        # Přidá do kontextu název akce pro formulář
        context = super().get_context_data(**kwargs)
        context['form_action'] = 'Vymazat vyšetření'  # Popis akce ve formuláři
        return context


# Zobrazení seznamu oznámení
class AnnouncementListView(ListView):
    template_name = 'announcement_list.html'
    model = Announcement  # Model pro načítání oznámení
    context_object_name = 'announcements'  # Název objektu v šabloně


# Zobrazení pro vytvoření nového oznámení
class AnnouncementCreateView(CreateView):
    template_name = 'announcement_form.html'
    form_class = AnnouncementForm  # Třída formuláře pro oznámení
    success_url = reverse_lazy('announcement_list')  # Přesměrování po úspěšném vytvoření


# Zobrazení pro aktualizaci oznámení
class AnnouncementUpdateView(UpdateView):
    template_name = 'announcement_form.html'
    form_class = AnnouncementForm  # Třída formuláře pro oznámení
    model = Announcement  # Model pro načítání a ukládání oznámení
    success_url = reverse_lazy('announcement_list')  # Přesměrování po úspěšné aktualizaci


# Zobrazení pro smazání oznámení
class AnnouncementDeleteView(DeleteView):
    template_name = 'announcement_confirm_delete.html'
    model = Announcement  # Model pro smazání oznámení
    success_url = reverse_lazy('announcement_list')  # Přesměrování po úspěšném smazání
