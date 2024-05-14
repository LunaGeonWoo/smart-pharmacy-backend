from django.contrib import admin
from .models import Receipt


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):

    list_display = (
        "medicine",
        "user",
    )

    list_filter = (
        "medicine",
        "created_at",
    )

    readonly_fields = ("created_at",)
