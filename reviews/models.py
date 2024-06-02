from django.db import models
from common.models import CommonModel


class Review(CommonModel):

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="환자",
    )
    medicine = models.ForeignKey(
        "medicines.Medicine",
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="약",
    )
    detail = models.TextField(
        verbose_name="댓글",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="댓글 단 시각",
    )

    def __str__(self) -> str:
        return self.created_at.strftime(
            "%Y년 %m월 %d일 %H시 %M분 %S초",
        )

    def __str__(self) -> str:
        return f"{self.user.username}님의 리뷰 ({self.medicine.name})"
