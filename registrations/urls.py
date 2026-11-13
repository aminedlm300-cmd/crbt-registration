
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("success/", views.registration_success, name="registration_success"),
    path("print-form/", views.print_registration, name="print_registration"),
]
