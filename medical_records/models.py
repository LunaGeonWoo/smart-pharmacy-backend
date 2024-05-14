from django.db import models
from common.models import CommonModel


class Record(CommonModel):

    name = models.CharField(
        max_length=150,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    m_record = models.ForeignKey(
        "medicines.Medicine",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.created_at.strftime(
            "%Y년 %m월 %d일 %H시 %M분 %S초",
        )
