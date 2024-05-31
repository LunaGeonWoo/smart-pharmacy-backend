from django.contrib import admin
from .models import Receipt


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):

    list_display = (
        "medicine",
        "owner",
    )

    list_filter = ("medicine",)

    readonly_fields = ("created_at",)
