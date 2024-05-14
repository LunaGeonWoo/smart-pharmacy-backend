from django.db import models
from common.models import CommonModel


class Medicine(CommonModel):
    name = models.CharField(
        max_length=150,
    )
    serial_number = models.PositiveBigIntegerField()
    efficacy = models.TextField(
        default="",
        blank=True,
    )
    usage = models.TextField(
        default="",
        blank=True,
    )
    need_to_know = models.TextField(
        default="",
        blank=True,
    )
    cautions = models.TextField(
        default="",
        blank=True,
    )
    beware_food = models.TextField(
        default="",
        blank=True,
    )
    side_effect = models.TextField(
        default="",
        blank=True,
    )
    how_to_store = models.TextField(
        default="",
        blank=True,
    )

    def __str__(self) -> str:
        return self.name
