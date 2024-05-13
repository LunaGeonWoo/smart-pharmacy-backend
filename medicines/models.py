from django.db import models
from common.models import CommonModel


class Medicines(CommonModel):
    name = models.CharField(
        max_length=150,
    )
