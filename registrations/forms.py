
from django import forms
from .models import PlayerRegistration


class PlayerRegistrationForm(forms.ModelForm):
    class Meta:
        model = PlayerRegistration
        fields = [
            "first_name_ar",
            "last_name_ar",
            "first_and_last_name_latin",
            "blood_group",
            "birth_date",
            "birth_place",
            "guardian_phone",
            "email",
        ]

        widgets = {
            "first_name_ar": forms.TextInput(attrs={
                "placeholder": "الاسم بالعربية",
            }),
            "last_name_ar": forms.TextInput(attrs={
                "placeholder": "اللقب بالعربية",
            }),
            "first_and_last_name_latin": forms.TextInput(attrs={
                "placeholder": "First and last name",
                "dir": "ltr",
            }),
            "blood_group": forms.TextInput(attrs={
                "placeholder": "blood group",
                "dir": "ltr",
            }),
            "birth_date": forms.DateInput(attrs={
                "type": "date",
            }),
            "birth_place": forms.TextInput(attrs={
                "placeholder": "مكان الميلاد",
            }),
            "guardian_phone": forms.TextInput(attrs={
                "placeholder": "رقم هاتف الولي",
                "type": "tel",
                "autocomplete": "tel",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "البريد الإلكتروني (اختياري)",
            }),
        }

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get("birth_date")
        from datetime import date

        if birth_date and birth_date > date.today():
            raise forms.ValidationError("تاريخ الميلاد لا يمكن أن يكون في المستقبل.")
        return birth_date
