from concurrent.futures._base import LOGGER

from django.shortcuts import render
from django import forms
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
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


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('user_list')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)
