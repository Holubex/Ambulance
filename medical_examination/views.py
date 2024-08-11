from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from medical_examination.forms import MedicalExaminationForm, AnnouncementForm
from medical_examination.models import MedicalExamination, Announcement
from patients.models import Patients, Role


# medical_examination

class MedicalExaminationFilterForm(forms.Form):
    patient = forms.ModelChoiceField(
        queryset=Patients.objects.filter(role_patient=Role.PATIENT),  # Přizpůsobte filtrování
        required=False,
        label='Pacient',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    nurse = forms.ModelChoiceField(
        queryset=Patients.objects.filter(role_patient=Role.NURSE),  # Přizpůsobte filtrování
        required=False,
        label='Sestřička',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    doctor = forms.ModelChoiceField(
        queryset=Patients.objects.filter(role_patient=Role.DOCTOR),  # Přizpůsobte filtrování
        required=False,
        label='Lékař',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    examination_date = forms.DateField(
        required=False,
        label='Datum vyšetření',
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    def filter(self, queryset):
        if self.is_valid():
            data = self.cleaned_data
            if data.get('patient'):
                queryset = queryset.filter(patient_id=data['patient'].id)
            if data.get('nurse'):
                queryset = queryset.filter(nurse_id=data['nurse'].id)
            if data.get('doctor'):
                queryset = queryset.filter(doctor_id=data['doctor'].id)
            if data.get('examination_date'):
                queryset = queryset.filter(examination_date=data['examination_date'])
        return queryset


class MedicalExaminationListView(ListView):
    template_name = 'medical_examination_list.html'
    model = MedicalExamination
    context_object_name = 'medical_examinations'
    permission_required = 'medical_examination.view_medical_examination'

    def get_queryset(self):
        form = MedicalExaminationFilterForm(self.request.GET)
        queryset = super().get_queryset()
        if form.is_valid():
            queryset = form.filter(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = MedicalExaminationFilterForm(self.request.GET)
        return context


class MedicalExaminationCreateView(CreateView):
    template_name = 'medical_examination_form.html'
    form_class = MedicalExaminationForm
    success_url = reverse_lazy('medical_examination_list')
    permission_required = 'medical_examination.add_medical_examination'


class MedicalExaminationDetailView(DetailView):
    template_name = 'medical_examination_detail.html'
    form_class = MedicalExamination
    context_object_name = 'medical_examination'


class AnnouncementListView(ListView):
    template_name = 'announcement_list.html'
    model = Announcement
    context_object_name = 'announcements'


class AnnouncementCreateView(CreateView):
    template_name = 'announcement_form.html'
    form_class = AnnouncementForm
    success_url = reverse_lazy('announcement_list')


class AnnouncementUpdateView(UpdateView):
    template_name = 'announcement_form.html'
    form_class = AnnouncementForm
    model = Announcement
    success_url = reverse_lazy('announcement_list')


class AnnouncementDeleteView(DeleteView):
    template_name = 'announcement_confirm_delete.html'
    model = Announcement
    success_url = reverse_lazy('announcement_list')
