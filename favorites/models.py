from django.db import models
from common.models import CommonModel


class Favorite(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="favorites",
        verbose_name="유저",
    )
    medicine = models.ForeignKey(
        "medicines.Medicine",
        on_delete=models.CASCADE,
        related_name="favorites",
        verbose_name="약",
    )

    def __str__(self) -> str:
        return f"{self.user.name} {self.medicine.name}"
