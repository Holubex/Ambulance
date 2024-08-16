# from concurrent.futures._base import LOGGER
#
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.mixins import PermissionRequiredMixin
# from django.shortcuts import render, redirect, get_object_or_404
# from django import forms
# from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
# from django.urls import reverse_lazy
#
# from patients.models import User
#
#
# # Create your views here.
# # Formulář pro model uživatele
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'  # Všechna pole modelu budou zahrnuta ve formuláři
#         labels = {
#             'name': 'Jméno',
#             'surname': 'Příjmení',
#             'email': 'Email',
#             'birth_date': 'Datum narození',
#             'birth_number': 'Rodné číslo',
#             'insurance': 'Pojišťovna',
#             'gender': 'Pohlaví',
#             'role_patient': 'Role uživatele',
#             'address': 'Adresa',
#             'contact': 'Kontakt'
#         }
#         help_texts = {
#             'birth_date': 'Zadejte datum ve formátu RRRR-MM-DD.'  # Pomocný text pro pole datum narození
#         }
#
#
# class UserListView(PermissionRequiredMixin, ListView):
#     model = User
#     template_name = 'user_list.html'  # Šablona pro zobrazení seznamu uživatelů
#     context_object_name = 'patients'
#     permission_required = 'patients.view_user'  # Požadované oprávnění pro zobrazení seznamu uživatelů
#
#     def get_queryset(self):
#         # Filtrovat uživatele podle role, pokud je specifikována v GET parametru
#         role = self.request.GET.get('role')
#         users = User.get_sorted_users()  # Použití statické metody pro lokalizované řazení
#         if role:
#             users = filter(lambda user: user.role_patient.lower() == role.lower(), users)
#         return users
#
#
# class UserDetailView(DetailView):
#     model = User
#     template_name = 'user_detail.html'  # Šablona pro zobrazení detailu uživatele
#     context_object_name = 'user'
#
#     def get_object(self):
#         # Načtení uživatele podle ID
#         return get_object_or_404(User, pk=self.kwargs['pk'])
#
#
# class UserCreateView(CreateView):
#     model = User
#     form_class = UserForm  # Formulář použitý pro vytvoření uživatele
#     template_name = 'create_user.html'
#     success_url = reverse_lazy('user_list')  # URL pro přesměrování po úspěšném vytvoření
#     permission_required = 'patients.add_user'  # Požadované oprávnění pro vytvoření uživatele
#
#     def form_invalid(self, form):
#         LOGGER.warning('User provided invalid data.')  # Zaznamenání varování, pokud je formulář neplatný
#         return super().form_invalid(form)
#
#
# class UserUpdateView(UpdateView):
#     template_name = 'create_user.html'
#     form_class = UserForm  # Formulář použitý pro úpravu uživatele
#     model = User
#     success_url = reverse_lazy('user_list')  # URL pro přesměrování po úspěšné úpravě
#     permission_required = 'patients.change_user'  # Požadované oprávnění pro úpravu uživatele


from concurrent.futures._base import LOGGER

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q

from patients.models import User, Role


# Formulář pro model uživatele
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'  # Všechna pole modelu budou zahrnuta ve formuláři
        labels = {
            'name': 'Jméno',
            'surname': 'Příjmení',
            'email': 'Email',
            'birth_date': 'Datum narození',
            'birth_number': 'Rodné číslo',
            'insurance': 'Pojišťovna',
            'gender': 'Pohlaví',
            'role_patient': 'Role uživatele',
            'address': 'Adresa',
            'contact': 'Kontakt'
        }
        help_texts = {
            'birth_date': 'Zadejte datum ve formátu RRRR-MM-DD.'  # Pomocný text pro pole datum narození
        }


class UserListView(PermissionRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'  # Šablona pro zobrazení seznamu uživatelů
    context_object_name = 'patients'
    permission_required = 'patients.view_user'  # Požadované oprávnění pro zobrazení seznamu uživatelů

    def get_queryset(self):
        # Získání parametrů z GET
        role = self.request.GET.get('role')
        search_query = self.request.GET.get('search', '')

        # Filtrovat uživatele podle role
        if role == 'patient':
            queryset = User.objects.filter(role_patient=Role.PATIENT)
        elif role == 'doctor':
            queryset = User.objects.filter(role_patient=Role.DOCTOR)
        elif role == 'nurse':
            queryset = User.objects.filter(role_patient=Role.NURSE)
        else:
            # Defaultně zobrazovat všechny uživatele
            queryset = User.objects.all()

        # Filtrujeme podle vyhledávacího dotazu
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(surname__icontains=search_query)
            )

        # Seřadíme výsledky podle příjmení a jména
        return queryset.order_by('surname', 'name')


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'  # Šablona pro zobrazení detailu uživatele
    context_object_name = 'user_detail'

    def get_object(self):
        # Načtení uživatele podle ID
        return get_object_or_404(User, pk=self.kwargs['pk'])


class UserCreateView(CreateView):
    model = User
    form_class = UserForm  # Formulář použitý pro vytvoření uživatele
    template_name = 'create_user.html'
    success_url = reverse_lazy('user_list')  # URL pro přesměrování po úspěšném vytvoření
    permission_required = 'patients.add_user'  # Požadované oprávnění pro vytvoření uživatele

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')  # Zaznamenání varování, pokud je formulář neplatný
        return super().form_invalid(form)


class UserUpdateView(UpdateView):
    template_name = 'create_user.html'
    form_class = UserForm  # Formulář použitý pro úpravu uživatele
    model = User
    success_url = reverse_lazy('user_list')  # URL pro přesměrování po úspěšné úpravě
    permission_required = 'patients.change_user'  # Požadované oprávnění pro úpravu uživatele
