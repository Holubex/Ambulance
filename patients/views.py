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
#
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
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
#             'birth_date': 'Zadejte datum ve formátu RRRR-MM-DD.'
#         }
#
#
# class UserListView(PermissionRequiredMixin, ListView):
#     model = User
#     template_name = 'user_list.html'
#     context_object_name = 'patients'
#     permission_required = 'patients.view_user'
#
#     def get_queryset(self):
#         # Filtrovat uživatele podle role, pokud je specifikována v GET parametru
#         role = self.request.GET.get('role')
#         queryset = User.objects.all()
#         if role:
#             queryset = queryset.filter(role_patient__iexact=role)
#         return queryset.order_by('surname', 'name')  # Explicitní řazení podle příjmení a jména
#
#
# class UserDetailView(PermissionRequiredMixin, DetailView):
#     model = User
#     template_name = 'user_detail.html'
#     context_object_name = 'user'
#     permission_required = 'patients.view_user'
#
#     def get_object(self):
#         # Načtení uživatele podle ID
#         return get_object_or_404(User, pk=self.kwargs['pk'])
#
#
# class UserCreateView(CreateView):
#     model = User
#     form_class = UserForm
#     template_name = 'create_user.html'
#     success_url = reverse_lazy('user_list')
#     permission_required = 'patients.add_user'
#
#     def form_invalid(self, form):
#         LOGGER.warning('User provided invalid data.')
#         return super().form_invalid(form)
#
#
# class UserUpdateView(UpdateView):
#     template_name = 'create_user.html'
#     form_class = UserForm
#     model = User
#     success_url = reverse_lazy('user_list')
#     permission_required = 'patients.change_user'
#
from concurrent.futures._base import LOGGER

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from patients.models import User


# Create your views here.

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
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
            'birth_date': 'Zadejte datum ve formátu RRRR-MM-DD.'
        }


class UserListView(PermissionRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'patients'
    permission_required = 'patients.view_user'

    def get_queryset(self):
        # Filtrovat uživatele podle role, pokud je specifikována v GET parametru
        role = self.request.GET.get('role')
        users = User.get_sorted_users()  # Použití statické metody pro lokalizované řazení
        if role:
            users = filter(lambda user: user.role_patient.lower() == role.lower(), users)
        return users

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'


    def get_object(self):
        # Načtení uživatele podle ID
        return get_object_or_404(User, pk=self.kwargs['pk'])


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('user_list')
    permission_required = 'patients.add_user'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class UserUpdateView(UpdateView):
    template_name = 'create_user.html'
    form_class = UserForm
    model = User
    success_url = reverse_lazy('user_list')
    permission_required = 'patients.change_user'

