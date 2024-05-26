from django.db import models
from common.models import CommonModel
from django.core import validators


class Medicine(CommonModel):
    serial_number = models.PositiveBigIntegerField(
        unique=True,
        verbose_name="품목일련번호",
    )
    name = models.CharField(
        max_length=150,
        verbose_name="제품명",
    )
    company = models.CharField(
        default="",
        max_length=150,
        verbose_name="업체명",
    )
    main_ingredient = models.TextField(
        default="",
        blank=True,
        verbose_name="주성분",
    )
    efficacy = models.TextField(
        default="",
        blank=True,
        verbose_name="이 약의 효능은 무엇입니까?",
    )
    usage = models.TextField(
        default="",
        blank=True,
        verbose_name="이 약은 어떻게 사용합니까?",
    )
    need_to_know = models.TextField(
        default="",
        blank=True,
        verbose_name="이 약을 사용하기 전에 반드시 알아야 할 내용은 무엇입니까?",
    )
    cautions = models.TextField(
        default="",
        blank=True,
        verbose_name="이 약의 사용상 주의사항은 무엇입니까?",
    )
    beware_food = models.TextField(
        default="",
        blank=True,
        verbose_name="이 약을 사용하는 동안 주의해야 할 약 또는 음식은 무엇입니까?",
    )
    side_effect = models.TextField(
        default="",
        blank=True,
        verbose_name="이 약은 어떤 이상반응이 나타날 수 있습니까?",
    )
    how_to_store = models.TextField(
        default="",
        blank=True,
        verbose_name="이 약은 어떻게 보관해야 합니까?",
    )
    price = models.PositiveIntegerField(
        default=0,
        validators=[validators.MinValueValidator(0)],
        verbose_name="가격",
    )

    def __str__(self) -> str:
        return self.name
