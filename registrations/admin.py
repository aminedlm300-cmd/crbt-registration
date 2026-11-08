
from django.contrib import admin
from .models import PlayerRegistration


@admin.register(PlayerRegistration)
class PlayerRegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "first_name_ar",
        "last_name_ar",
        "first_and_last_name_latin",
        "blood_group",
        "birth_date",
        "guardian_phone",
        "status",
        "created_at",
    )

    list_filter = ("status", "created_at")
    search_fields = (
        "first_name_ar",
        "last_name_ar",
        "first_and_last_name_latin",
        "blood group",
        "guardian_phone",
        "email",
    )

    list_editable = ("status",)
    readonly_fields = ("created_at",)
