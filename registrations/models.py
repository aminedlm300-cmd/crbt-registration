
from django.db import models


class PlayerRegistration(models.Model):
    STATUS_CHOICES = [
        ("pending", "قيد المراجعة"),
        ("accepted", "مقبول"),
        ("rejected", "مرفوض"),
    ]

    first_name_ar = models.CharField("الاسم بالعربية", max_length=100)
    last_name_ar = models.CharField("اللقب بالعربية", max_length=100)

    first_and_last_name_latin = models.CharField("الاسم و اللقب باللاتينية", max_length=100)
    blood_group = models.CharField("الزمرة الدموية", max_length=100)

    birth_date = models.DateField("تاريخ الازدياد")
    birth_place = models.CharField(
    max_length=100,
    verbose_name="مكان الميلاد",
    blank=True,
    default=""
)
    guardian_phone = models.CharField("رقم هاتف الولي", max_length=25)
    email = models.EmailField(blank=True, verbose_name="البريد الإلكتروني")

    status = models.CharField(
        "حالة الطلب",
        max_length=10,
        choices=STATUS_CHOICES,
        default="pending",
    )

    created_at = models.DateTimeField("تاريخ التسجيل", auto_now_add=True)

    class Meta:
        verbose_name = "تسجيل لاعب"
        verbose_name_plural = "تسجيلات اللاعبين"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name_ar} {self.last_name_ar}"
