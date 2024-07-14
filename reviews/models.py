from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
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
    rating = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ],
        verbose_name="평점",
    )

    def __str__(self) -> str:
        return f"{self.user.username}님의 리뷰 ({self.medicine.name})"
