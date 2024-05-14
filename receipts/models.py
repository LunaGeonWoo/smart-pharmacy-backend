from django.db import models
from common.models import CommonModel


class Receipt(CommonModel):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="구매 시각",
    )
    medicine = models.ForeignKey(
        "medicines.Medicine",
        on_delete=models.SET_DEFAULT,
        default=1,
        verbose_name="약",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="환자",
    )

    def get_purchase_time(self):
        return self.created_at.strftime(
            "%Y년 %m월 %d일 %H시 %M분 %S초",
        )

    def __str__(self) -> str:
        return f"{self.medicine.name} / {self.user.name}"
