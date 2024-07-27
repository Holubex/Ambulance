from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from medical_examination.forms import MedicalExaminationForm
from medical_examination.models import MedicalExamination


class MedicalExaminationListView(ListView):
    template_name = 'medical_examination_list.html'
    model = MedicalExamination
    context_object_name = 'medical_examinations'
    permission_required = 'medical_examination.view_medical_examination'

class MedicalExaminationCreateView(CreateView):
    template_name = 'medical_examination_form.html'
    form_class = MedicalExaminationForm
    success_url = reverse_lazy('medical_examination_list')
    permission_required = 'medical_examination.add_medical_examination'


class MedicalExaminationDetailView(DetailView):
    template_name = 'medical_examination_detail.html'
    form_class = MedicalExamination
    context_object_name = 'medical_examination'


    # def get(self, request, pk):
        # if MedicalExamination.filter(id=pk).exists():
        #     result = MedicalExamination.objects.get(id=pk)
        #     return render(request, 'medical_examination_list.html', {'examinations': examinations})

# class MedicalExaminationCreateView(View):
#     def get(self, request):
#         form = MedicalExaminationForm()
#         return render(request, 'medical_examination/examination_form.html', {'form': form})
#
#     def post(self, request):
#         form = MedicalExaminationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('medical_examination_list')
#         return render(request, 'medical_examination/examination_form.html', {'form': form})
