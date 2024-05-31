from django.db import models
from common.models import CommonModel
from django.core.validators import MinValueValidator


class Inventory(CommonModel):
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="inventory",
    )
    medicine = models.ForeignKey(
        "medicines.Medicine",
        on_delete=models.CASCADE,
        related_name="inventory",
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
    )

    def __str__(self):
        return f"{self.owner.username}의 {self.medicine.name} {self.quantity}개"

    class Meta:
        verbose_name_plural = "Inventories"
