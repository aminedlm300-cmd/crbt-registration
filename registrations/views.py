
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PlayerRegistrationForm
from .models import PlayerRegistration


def home(request):
    if request.method == "POST":
        form = PlayerRegistrationForm(request.POST)

        if form.is_valid():
            registration = form.save()

            # Keep this registration linked to the visitor's session
            request.session["print_registration_id"] = registration.pk

            return redirect("registration_success")
    else:
        form = PlayerRegistrationForm()

    return render(request, "registrations/home.html", {
        "form": form,
        "submitted": False,
    })


def registration_success(request):
    return render(request, "registrations/home.html", {
        "form": PlayerRegistrationForm(),
        "submitted": True,
    })


def print_registration(request):
    registration_id = request.session.get("print_registration_id")

    if not registration_id:
        return redirect("home")

    registration = get_object_or_404(
        PlayerRegistration,
        pk=registration_id
    )

    return render(request, "registrations/print_form.html", {
        "registration": registration,
    })
