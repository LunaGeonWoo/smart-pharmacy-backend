from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "created_at",
        "detail",
        "rating",
    )

    list_filter = (
        "medicine",
        "created_at",
        "rating",
    )
