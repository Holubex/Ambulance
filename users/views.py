from concurrent.futures._base import LOGGER

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from users.models import User
# Create your views here.


# Definice view pro úvodní stránku
def home(request):
    return render(request, 'home.html',
                  {'title': 'Welcome to HollyMovies'})


# Definice formuláře pro model User pomocí ModelForm
class UserForm(forms.ModelForm):

    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Datum narození')

    class Meta:
        model = User # Určuje model, který se použije
        fields = '__all__'


# Definice view pro zobrazení seznamu uživatelů, vyžadující oprávnění
class UserListView(PermissionRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html' # Určuje šablonu, která se vykreslí
    context_object_name = 'users'  # Název kontextové proměnné, která se použije v šabloně
    permission_required = 'users.add_user' # Oprávnění, které je vyžadováno pro zobrazení této view

    def get_queryset(self):
        # Filtrovat uživatele podle role, pokud je specifikována v GET parametru
        role = self.request.GET.get('role')
        if role:
            return User.objects.filter(role_patient__iexact=role)
        return User.objects.all()


class UserDetailView(PermissionRequiredMixin, DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'
    permission_required = 'users.view_user'

    def get_object(self):
        # Načtení uživatele podle ID
        return get_object_or_404(User, pk=self.kwargs['pk'])

# Definice view pro vytvoření nového uživatele
class UserCreateView(CreateView):
    model = User 
    form_class = UserForm  # Určuje formulář, který se použije
    template_name = 'create_user.html'  
    success_url = reverse_lazy('user_list')  # URL, na kterou se přesměruje po úspěšném odeslání formuláře
    permission_required = 'users.add_user'  

    # Přepis metody form_invalid, která se volá, pokud je formulář neplatný
    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')  # Zaloguje varování
        return super().form_invalid(form)  # Zavolá původní metodu form_invalid z třídy CreateView
