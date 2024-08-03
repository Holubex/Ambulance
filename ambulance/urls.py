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

from objednavkovy_kalendar.views import AppointmentListView, Kontakt, Nase_sluzby, Prakticke_informace, \
    AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView
from users.views import UserCreateView, UserListView, home, nase_sluzby
from accounts.views import SubmittableLoginView, RegisterView
from users.views import UserCreateView, UserListView, home, UserDetailView
from accounts.views import SubmittableLoginView, RegistrationForm, RegisterView
from medical_examination.views import (
    MedicalExaminationListView,
    MedicalExaminationCreateView,
    MedicalExaminationDetailView,
    AnnouncementListView,
    AnnouncementCreateView,
    AnnouncementUpdateView,
    AnnouncementDeleteView,
)

from objednavkovy_kalendar.views import (
    AppointmentListView, 
    AppointmentCreateView, 
    AppointmentUpdateView, 
    AppointmentDeleteView
)





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('create_user/', UserCreateView.as_view(), name='create_user'),
    path('user-list/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),

    path('medical-examination-list/', MedicalExaminationListView.as_view(), name='medical_examination_list'),
    path('medical-examination-create/', MedicalExaminationCreateView.as_view(), name='medical_examination_create'),
    path('medical-examinations/', MedicalExaminationListView.as_view(), name='medical_examination_list'),
    path('medical-examination-detail/<pk>/', MedicalExaminationDetailView.as_view(), name='medical_examination_detail'),


    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    path('announcements/', AnnouncementListView.as_view(), name='announcement_list'),
    path('announcements/new/', AnnouncementCreateView.as_view(), name='announcement_create'),
    path('announcements/<pk>/edit/', AnnouncementUpdateView.as_view(), name='announcement_edit'),
    path('announcements/<pk>/delete/', AnnouncementDeleteView.as_view(), name='announcement_delete'),

    path('objednavka/', AppointmentListView.as_view(), name='appointment_list'),
    path('objednavka/new/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('objednavka/<pk>/edit/', AppointmentUpdateView.as_view(), name='appointment_edit'),
    path('objednavka/<pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete'),
    path('kontakt/', Kontakt.as_view(), name='kontakt'),
    path('nase_sluzby/', Nase_sluzby.as_view(), name='nase_sluzby'),
    path('prakticke_informace/', Prakticke_informace.as_view(), name='prakticke_informace'),
]
