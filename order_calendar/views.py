from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.urls import reverse_lazy
from .models import Appointment
from .forms import AppointmentForm
from django.http import JsonResponse


class AppointmentListView(ListView):
    model = Appointment  # Určuje model, který se použije
    template_name = "appointment_list.html"  # Určuje šablonu, která se vykreslí
    context_object_name = (
        "appointments"  # Název kontextové proměnné, která se použije v šabloně
    )

    # Přepis metody get, aby zpracovávala jak běžné, tak AJAXové požadavky
    def get(self, request, *args, **kwargs):
        if (
                request.headers.get("x-requested-with") == "XMLHttpRequest"
        ):  # Kontroluje, zda je požadavek AJAXový
            appointments = list(
                Appointment.objects.select_related("doctor", "patient").values(
                    "id",
                    "doctor__username",
                    "patient__username",
                    "service",
                    "day",
                    "time",
                    "time_ordered",
                )
            )  # Načítá appointments s příbuznými údaji o doktorovi a pacientovi

            # Převádí pole day a time na start a end pro JSON odpověď
            for appointment in appointments:
                appointment["start"] = appointment.pop("day").isoformat()
                appointment["end"] = appointment.pop("time")
            return JsonResponse(
                appointments, safe=False
            )  # Vrací data jako JSON pro AJAXové požadavky
        return super().get(
            request, *args, **kwargs
        )  # Zpracovává neAJAXové požadavky pomocí výchozího chování ListView


# Tato view založená na třídách zpracovává vytvoření nového objektu Appointment
class AppointmentCreateView(CreateView):
    model = Appointment  # Určuje model, který se použije
    form_class = AppointmentForm  # Určuje formulář, který se použije
    template_name = "appointment_form.html"  # Určuje šablonu, která se vykreslí
    success_url = reverse_lazy(
        "appointment_list"
    )  # URL, na kterou se přesměruje po úspěšném odeslání formuláře

    # Přepis metody form_valid, aby zpracovávala AJAXové požadavky
    def form_valid(self, form):
        print("Form is valid")
        print("Form data:", form.cleaned_data)
        response = super().form_valid(form)
        if (
                self.request.headers.get("x-requested-with") == "XMLHttpRequest"
        ):  # Kontroluje, zda je požadavek AJAXový
            appointment = form.save()
            data = {
                "status": "success",
                "appointment": {
                    "id": appointment.id,
                    "doctor": appointment.doctor.surname,
                    "service": appointment.service,
                    "day": appointment.day,
                    "time": appointment.time,
                    "time_ordered": appointment.time_ordered,
                },
            }
            return JsonResponse(data)  # Vrací data jako JSON pro AJAXové požadavky
        return response  # Zpracovává neAJAXové požadavky pomocí výchozího chování

    # Přepis metody form_invalid, aby zpracovávala AJAXové požadavky
    def form_invalid(self, form):
        print("Form is invalid")
        print("Form errors:", form.errors)
        response = super().form_invalid(form)
        if (
                self.request.headers.get("x-requested-with") == "XMLHttpRequest"
        ):  # Kontroluje, zda je požadavek AJAXový
            return JsonResponse(
                {"status": "error", "errors": form.errors}
            )  # Vrací chyby formuláře jako JSON
        return response  # Zpracovává neAJAXové požadavky pomocí výchozího chování


# Tato view založená na třídách zpracovává aktualizaci existujícího objektu Appointment
class AppointmentUpdateView(UpdateView):
    model = Appointment  # Určuje model, který se použije
    form_class = AppointmentForm  # Určuje formulář, který se použije
    template_name = "appointment_form.html"  # Určuje šablonu, která se vykreslí
    success_url = reverse_lazy(
        "appointment_list"
    )  # URL, na kterou se přesměruje po úspěšné aktualizaci


# Tato view založená na třídách zpracovává smazání existujícího objektu Appointment
class AppointmentDeleteView(DeleteView):
    model = Appointment  # Určuje model, který se použije
    template_name = (
        "appointment_confirm_delete.html"  # Určuje šablonu, která se vykreslí
    )
    success_url = reverse_lazy(
        "appointment_list"
    )  # URL, na kterou se přesměruje po úspěšném smazání
