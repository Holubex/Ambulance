from django.forms import ModelForm

from medical_examination.models import MedicalExamination, Announcement


class MedicalExaminationForm(ModelForm):
    class Meta:
        model = MedicalExamination
        fields = "__all__"
        labels = {
            "patient": "Pacient",
            "nurse": "Zdravotní sestra",
            "doctor": "Doktor",
            "current_complaints": "Aktuální obtíže",
            "objective_findings": "Objektivní nález",
            "diagnosis": "Diagnóza",
            "prescription": "Recept",
        }


class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ["title", "content"]
        labels = {
            "title": "Nadpis",
            "content": "Obsah",
        }
