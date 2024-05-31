from django.contrib import admin
from .models import Receipt


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):

    list_display = (
        "medicine",
        "quantity",
        "owner",
    )

    list_filter = ("medicine",)

    readonly_fields = ("purchase_at",)
