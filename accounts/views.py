from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile
from django.views import View
from django import forms
from django.contrib.auth.models import User


# Zde definujeme vlastní pohledy

class SubmittableLoginView(LoginView):
    # Nastavení šablony pro přihlášení
    template_name = "login.html"


class RegistrationForm(UserCreationForm):
    # Přidání pole pro datum narození do formuláře
    birth_date = forms.DateField(
        required=False, widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        # Definování modelu a polí, která budou ve formuláři
        model = User
        fields = ["username", "password1", "password2", "email", "birth_date"]

    def save(self, commit=True):
        # Uložení uživatele s rozšířenými údaji (email, datum narození)
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            # Vytvoření a uložení profilu
            profile = Profile(user=user, birth_date=self.cleaned_data["birth_date"])
            profile.save()
        return user


class RegisterView(View):
    def get(self, request):
        # Zobrazení registračního formuláře
        form = RegistrationForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        # Zpracování dat z registračního formuláře
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Přesměrování na domovskou stránku po úspěšné registraci
            return redirect("home")
        # Opětovné zobrazení formuláře s chybami
        return render(request, "register.html", {"form": form})
