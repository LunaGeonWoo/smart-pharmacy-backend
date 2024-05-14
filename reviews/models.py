from django.db import models
from common.models import CommonModel


class Review(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    medicine = models.ForeignKey(
        "medicines.Medicine",
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    detail = models.TextField()

    def __str__(self) -> str:
        return f"{self.user.name} / {self.medicine.name}"
