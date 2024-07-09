from django.db import models
from common.models import CommonModel
from django.core.validators import MinValueValidator


class Inventory(CommonModel):
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="inventories",
    )
    medicine = models.ForeignKey(
        "medicines.Medicine",
        on_delete=models.CASCADE,
        related_name="inventories",
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
    )

    def __str__(self):
        return f"{self.owner}의 장바구니"

    class Meta:
        verbose_name_plural = "Inventories"
