
from django.shortcuts import render, redirect

from .forms import PlayerRegistrationForm


def home(request):
    submitted = False

    if request.method == "POST":
        form = PlayerRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("registration_success")
    else:
        form = PlayerRegistrationForm()

    return render(request, "registrations/home.html", {
        "form": form,
        "submitted": submitted,
    })


def registration_success(request):
    return render(request, "registrations/home.html", {
        "form": PlayerRegistrationForm(),
        "submitted": True,
    })
