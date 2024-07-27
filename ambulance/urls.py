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
from medical_examination.views import MedicalExaminationListView
from users.views import UserCreateView, UserListView, home
from accounts.views import SubmittableLoginView, RegistrationForm, RegisterView
from medical_examination.views import (
    MedicalExaminationListView,
    MedicalExaminationCreateView,
    MedicalExaminationDetailView
)
from users.views import UserCreateView, UserListView, home





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('create_user/', UserCreateView.as_view(), name='create_user'),
    path('user-list/', UserListView.as_view(), name='user_list'),

    path('medical-examination-list/', MedicalExaminationListView.as_view(), name='medical_examination_list'),
    path('medical-examination-create/', MedicalExaminationCreateView.as_view(), name='medical_examination_create'),
    path('medical-examination-detail/<pk>/', MedicalExaminationDetailView.as_view(), name='medical_examination_detail'),


    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
