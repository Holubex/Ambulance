"""ambulance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

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

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("create_user/", UserCreateView.as_view(), name="create_user"),
    path("user-list/", UserListView.as_view(), name="user_list"),
    path("patients/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("patients/edit/<int:pk>/", UserUpdateView.as_view(), name="user_edit"),
    path(
        "medical-examination-list/",
        MedicalExaminationListView.as_view(),
        name="medical_examination_list",
    ),
    path(
        "medical-examination-create/",
        MedicalExaminationCreateView.as_view(),
        name="medical_examination_create",
    ),
    path(
        "medical-examinations/",
        MedicalExaminationListView.as_view(),
        name="medical_examination_list",
    ),
    path(
        "medical-examination-detail/<pk>/",
        MedicalExaminationDetailView.as_view(),
        name="medical_examination_detail",
    ),
    path(
        'medical-examination/edit/<pk>/',
        MedicalExaminationUpdateView.as_view(),
        name='medical_examination_edit'
    ),
    path(
        'medical-examination/delete/<pk>/',
         MedicalExaminationDeleteView.as_view(),
         name='medical_examination_delete'
    ),
    path("accounts/register/", RegisterView.as_view(), name="register"),
    path("accounts/login/", SubmittableLoginView.as_view(), name="login"),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(next_page="home"),
        name="logout",
    ),
    path("announcements/", AnnouncementListView.as_view(), name="announcement_list"),
    path(
        "announcements/new/",
        AnnouncementCreateView.as_view(),
        name="announcement_create",
    ),
    path(
        "announcements/<pk>/edit/",
        AnnouncementUpdateView.as_view(),
        name="announcement_edit",
    ),
    path(
        "announcements/<pk>/delete/",
        AnnouncementDeleteView.as_view(),
        name="announcement_delete",
    ),
    path("appointment/", AppointmentListView.as_view(), name="appointment_list"),
    path(
        "appointment/new/", AppointmentCreateView.as_view(), name="appointment_create"
    ),
    path(
        "appointment/<pk>/edit/",
        AppointmentUpdateView.as_view(),
        name="appointment_edit",
    ),
    path(
        "appointment/<pk>/delete/",
        AppointmentDeleteView.as_view(),
        name="appointment_delete",
    ),
    path("contact/", ContactView.as_view(), name="contact"),
    path("our_services/", OurServicesView.as_view(), name="our_services"),
    path("practical_info/", PracticalInfoView.as_view(), name="practical_info"),
]
