from django.db import models
from common.models import CommonModel
from django.core import validators


class Cart(CommonModel):
    user = models.ForeignKey("users.User")

    def __str__(self):
        return f"{self.user.name}의 장바구니"


class CartItem(CommonModel):

    medicine = models.ForeignKey("medicines.Medicine")
    cart = models.ForeignKey("cart.Cart")
    quantity = models.PositiveIntegerField(validators=[validators.MinValueValidator(1)])

    def __str__(self):
        return f"{self.medicine.name} X {self.quantity}"
