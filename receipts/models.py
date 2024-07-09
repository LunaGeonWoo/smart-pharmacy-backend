from django.db import models
from django.core.validators import MinValueValidator


class Receipt(models.Model):
    purchase_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="구매 시각",
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="주인",
    )

    def get_total_price(self):
        return self.quantity * self.past_medicine.price_per_medicine_at_purchase

    def __str__(self) -> str:
        return f"{self.owner.name}의 영수증 {self.purchase_at}"


class PastMedicine(models.Model):
    receipt = models.ForeignKey(
        Receipt,
        on_delete=models.CASCADE,
        related_name="past_medicine",
    )
    medicine = models.ForeignKey(
        "medicines.Medicine",
        on_delete=models.SET_DEFAULT,
        default=1,
        verbose_name="약",
    )
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name="개수",
    )
    price_per_medicine_at_purchase = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="구매 당시 하나 당 가격",
    )

    def __str__(self) -> str:
        return f"{self.medicine.name} {self.quantity}개 / {self.receipt.owner.name}"
