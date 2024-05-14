from django.db import models
from common.models import CommonModel


class Receipt(CommonModel):
    medicine = models.ForeignKey(
        "medicines.Medicine",
        on_delete=models.SET_DEFAULT,
        default=1,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.medicine.name} / {self.user.name}"
