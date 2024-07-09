from django.contrib import admin
from .models import Receipt, PastMedicine


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):

    list_display = (
        "owner",
        "purchase_at",
    )

    readonly_fields = ("purchase_at",)


@admin.register(PastMedicine)
class ReceiptAdmin(admin.ModelAdmin):

    list_display = (
        "medicine",
        "quantity",
        "price_per_medicine_at_purchase",
    )

    list_filter = ("medicine",)
