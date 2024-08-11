from django.contrib import admin

# Register your models here.
from patients.models import Patients

admin.site.register(Patients)