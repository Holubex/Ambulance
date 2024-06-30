from django.shortcuts import render
from django.views.generic import ListView

from medical_examination.models import MedicalExamination


class MedicalExaminationListView(ListView):
    template_name = 'medical_examination_list.html'
    model = MedicalExamination
    context_object_name = 'medical_examinations'


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
