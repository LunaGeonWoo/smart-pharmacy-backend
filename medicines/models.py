from django.db import models
from common.models import CommonModel


class Medicine(CommonModel):
    serial_number = models.PositiveBigIntegerField(
        unique=0,
    )
    name = models.CharField(
        max_length=150,
    )
    company = models.CharField(
        default="",
        max_length=150,
    )
    main_ingredient = models.TextField(
        default="",
        blank=True,
    )
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
