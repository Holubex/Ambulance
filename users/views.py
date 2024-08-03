from concurrent.futures._base import LOGGER

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from users.models import User
# Create your views here.


def home(request):
    return render(request, 'home.html',
                  {'title': 'Welcome to HollyMovies'})


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserListView(PermissionRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'
    permission_required = 'users.add_user'

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

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('user_list')
    permission_required = 'users.add_user'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)

from django.shortcuts import render

def nase_sluzby(request):
    return render(request, 'nase_sluzby.html', {'title': 'Naše služby'})



