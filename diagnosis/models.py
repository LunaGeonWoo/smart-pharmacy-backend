from django.db import models
from common.models import CommonModel
from users.models import User


class Diagnosis(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    prompt = models.TextField()
    result = models.TextField()

    def __str__(self) -> str:
        return f"{self.user.username}님의 진단"
