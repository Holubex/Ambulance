from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from medical_examination.forms import MedicalExaminationForm, AnnouncementForm
from medical_examination.models import MedicalExamination, Announcement


# Zobrazuje seznam všech lékařských vyšetření
class MedicalExaminationListView(ListView):
    template_name = "medical_examination_list.html"
    model = MedicalExamination
    context_object_name = "medical_examinations"
    permission_required = "medical_examination.view_medical_examination"


# Umožňuje vytvořit nové lékařské vyšetření
class MedicalExaminationCreateView(CreateView):
    template_name = "medical_examination_form.html"
    form_class = MedicalExaminationForm
    success_url = reverse_lazy("medical_examination_list")
    permission_required = "medical_examination.add_medical_examination"


# Zobrazuje detail konkrétního lékařského vyšetření
class MedicalExaminationDetailView(DetailView):
    template_name = "medical_examination_detail.html"
    form_class = MedicalExamination
    context_object_name = "medical_examination"


# Zobrazuje seznam všech oznámení
class AnnouncementListView(ListView):
    template_name = "announcement_list.html"
    model = Announcement
    context_object_name = "announcements"


# Umožňuje vytvořit nové oznámení
class AnnouncementCreateView(CreateView):
    template_name = "announcement_form.html"
    form_class = AnnouncementForm
    success_url = reverse_lazy("announcement_list")


# Umožňuje aktualizovat existující oznámení
class AnnouncementUpdateView(UpdateView):
    template_name = "announcement_form.html"
    form_class = AnnouncementForm
    model = Announcement
    success_url = reverse_lazy("announcement_list")


# Umožňuje smazat existující oznámení
class AnnouncementDeleteView(DeleteView):
    template_name = "announcement_confirm_delete.html"
    model = Announcement
    success_url = reverse_lazy("announcement_list")
