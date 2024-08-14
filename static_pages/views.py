from django.shortcuts import render
from django.views.generic import TemplateView


# Vytváří zde své pohledy (views).
def home(request):
    # Zpracovává žádost o domovskou stránku a vrací HTML šablonu 'home.html'
    # s titulkem 'Vítejte na stránkách psychiatrie Hnídek'
    return render(request, 'home.html',
                  {'title': 'Vítejte na stránkách psychiatrie Hnídek'})


class ContactView(TemplateView):
    # Definice pohledu pro stránku kontaktů, která používá šablonu 'contact.html'
    template_name = 'contact.html'


class OurServicesView(TemplateView):
    # Definice pohledu pro stránku "Naše služby", která používá šablonu 'our_services.html'
    template_name = 'our_services.html'


class PracticalInfoView(TemplateView):
    # Definice pohledu pro stránku s praktickými informacemi, která používá šablonu 'practical_info.html'
    template_name = 'practical_info.html'

