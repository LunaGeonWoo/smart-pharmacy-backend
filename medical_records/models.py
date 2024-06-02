from django.db import models
from common.models import CommonModel


class MedicalRecord(CommonModel):

    name = models.CharField(
        max_length=150,
        verbose_name="증상",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="환자",
    )

    m_record = models.ForeignKey(
        "medicines.Medicine",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="약",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="진료 받은 시각",
    )

    def __str__(self) -> str:
        return self.created_at.strftime(
            "%Y년 %m월 %d일 %H시 %M분 %S초",
        )
