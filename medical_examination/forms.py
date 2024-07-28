from django.forms import ModelForm

from medical_examination.models import MedicalExamination, Announcement


class MedicalExaminationForm(ModelForm):
    class Meta:
        model = MedicalExamination
        fields = '__all__'


class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']
        labels = {
            'title': 'Nadpis',
            'content': 'Obsah',
        }