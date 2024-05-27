from django.db import models
from common.models import CommonModel
from django.core import validators


class Cart(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user.name}의 장바구니"


class CartItem(CommonModel):

    medicine = models.ForeignKey(
        "medicines.Medicine",
        on_delete=models.CASCADE,
    )
    cart = models.ForeignKey(
        "carts.Cart",
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(validators=[validators.MinValueValidator(1)])

    def __str__(self):
        return f"{self.medicine.name} X {self.quantity}"
