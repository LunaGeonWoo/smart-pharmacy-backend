from django.contrib import admin
from .models import MedicalRecord


@admin.register(MedicalRecord)
class RecordAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "user",
        "m_record",
        "created_at",
    )

    list_filter = (
        "name",
        "m_record",
    )

    readonly_fields = ("created_at",)
