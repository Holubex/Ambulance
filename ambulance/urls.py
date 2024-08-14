# Importy potřebné pro konfiguraci URL
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

# Importy pohledů (views) z různých aplikací
from patients.views import UserCreateView, UserListView, UserDetailView, UserUpdateView
from accounts.views import SubmittableLoginView, RegistrationForm, RegisterView
from medical_examination.views import (
    MedicalExaminationListView,
    MedicalExaminationCreateView,
    MedicalExaminationDetailView,
    MedicalExaminationUpdateView,
    MedicalExaminationDeleteView,
    AnnouncementListView,
    AnnouncementCreateView,
    AnnouncementUpdateView,
    AnnouncementDeleteView,
)
from order_calendar.views import (
    AppointmentListView,
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentDeleteView,
)
from static_pages.views import ContactView, OurServicesView, PracticalInfoView, home

# Seznam URL a jejich odpovídající pohledy (views)
urlpatterns = [
    # Cesta k administračnímu rozhraní Django
    path("admin/", admin.site.urls),
    
    # Hlavní stránka webu
    path("", home, name="home"),
    
    # URL pro správu uživatelů
    path("create_user/", UserCreateView.as_view(), name="create_user"),  # Vytvoření nového uživatele
    path("user-list/", UserListView.as_view(), name="user_list"),  # Seznam všech uživatelů
    path("patients/<int:pk>/", UserDetailView.as_view(), name="user_detail"),  # Detail uživatele
    path("patients/edit/<int:pk>/", UserUpdateView.as_view(), name="user_edit"),  # Úprava uživatele
    
    # URL pro správu lékařských vyšetření
    path("medical-examination-list/", MedicalExaminationListView.as_view(), name="medical_examination_list"),  # Seznam lékařských vyšetření
    path("medical-examination-create/", MedicalExaminationCreateView.as_view(), name="medical_examination_create"),  # Vytvoření nového vyšetření
    path("medical-examinations/", MedicalExaminationListView.as_view(), name="medical_examination_list"),  # Opakování seznamu vyšetření
    path("medical-examination-detail/<pk>/", MedicalExaminationDetailView.as_view(), name="medical_examination_detail"),  # Detail vyšetření
    path('medical-examination/edit/<pk>/', MedicalExaminationUpdateView.as_view(), name='medical_examination_edit'),  # Úprava vyšetření
    path('medical-examination/delete/<pk>/', MedicalExaminationDeleteView.as_view(), name='medical_examination_delete'),  # Smazání vyšetření
    
    # URL pro správu uživatelských účtů
    path("accounts/register/", RegisterView.as_view(), name="register"),  # Registrace nového uživatele
    path("accounts/login/", SubmittableLoginView.as_view(), name="login"),  # Přihlášení
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),  # Odhlášení
    
    # URL pro správu oznámení
    path("announcements/", AnnouncementListView.as_view(), name="announcement_list"),  # Seznam oznámení
    path("announcements/new/", AnnouncementCreateView.as_view(), name="announcement_create"),  # Vytvoření nového oznámení
    path("announcements/<pk>/edit/", AnnouncementUpdateView.as_view(), name="announcement_edit"),  # Úprava oznámení
    path("announcements/<pk>/delete/", AnnouncementDeleteView.as_view(), name="announcement_delete"),  # Smazání oznámení
    
    # URL pro správu schůzek
    path("appointment/", AppointmentListView.as_view(), name="appointment_list"),  # Seznam schůzek
    path("appointment/new/", AppointmentCreateView.as_view(), name="appointment_create"),  # Vytvoření nové schůzky
    path("appointment/<pk>/edit/", AppointmentUpdateView.as_view(), name="appointment_edit"),  # Úprava schůzky
    path("appointment/<pk>/delete/", AppointmentDeleteView.as_view(), name="appointment_delete"),  # Smazání schůzky
    
    # URL pro statické stránky
    path("contact/", ContactView.as_view(), name="contact"),  # Kontaktní formulář
    path("our_services/", OurServicesView.as_view(), name="our_services"),  # Naše služby
    path("practical_info/", PracticalInfoView.as_view(), name="practical_info"),  # Praktické informace
]