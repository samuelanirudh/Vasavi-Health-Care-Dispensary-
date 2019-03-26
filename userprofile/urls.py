from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from allauth.account.views import LoginView, SignupView, LogoutView
from . import views
from .views import PatientDetailsView

app_name = 'userprofile'

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/profile/', PatientDetailsView.as_view(), name='index'),
    path('accounts/profile/create/', views.create, name='create'),
]
