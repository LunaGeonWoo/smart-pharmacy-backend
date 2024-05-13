from django.db import models
from common.models import CommonModel


class Receipt(CommonModel):
    medicine = models.ForeignKey(
        "medicines.Medicine",
    )

    user = models.ForeignKey(
        "users.User",
    )
