from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def home(request):
    return render(request, 'home.html',
                  {'title': 'Vítejte na stránkách psychiatrie Hnídek'})


class ContactView(TemplateView):
    template_name = 'contact.html'


class OurServicesView(TemplateView):
    template_name = 'our_services.html'


class PracticalInfoView(TemplateView):
    template_name = 'practical_info.html'
