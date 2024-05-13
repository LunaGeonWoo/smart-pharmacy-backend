from django.db import models
from common.models import CommonModel


class Medicine(CommonModel):
    name = models.CharField(
        max_length=150,
    )

    def __str__(self) -> str:
        return self.name
