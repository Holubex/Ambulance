from django.forms import ModelForm

from medical_examination.models import MedicalExamination


class MedicalExaminationForm(ModelForm):
    class Meta:
        model = MedicalExamination
        fields = '__all__'