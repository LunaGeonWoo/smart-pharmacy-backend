from django.contrib import admin
from .models import Receipt, PastMedicine


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):

    list_display = (
        "owner",
        "purchase_at",
    )


@admin.register(PastMedicine)
class PastMedicineAdmin(admin.ModelAdmin):
    def owner(self, past_medicine):
        return past_medicine.receipt.owner

    list_display = (
        "medicine",
        "owner",
        "price_per_medicine_at_purchase",
    )

    list_filter = ("medicine",)
