from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile
from django.views import View
from django import forms
from django.contrib.auth.models import User
# Create your views here.


class SubmittableLoginView(LoginView):
    template_name = 'login.html'


class RegistrationForm(UserCreationForm):
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'birth_date']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = Profile(user=user, birth_date=self.cleaned_data['birth_date'])
            profile.save()
        return user


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'register.html', {'form': form})