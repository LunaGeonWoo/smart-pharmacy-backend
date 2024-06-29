from django.db import models
from common.models import CommonModel


class Diagnose(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        default="Untitled",
        max_length=100,
    )

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Diagnosis"


class Query(CommonModel):
    prompt = models.TextField()
    result = models.TextField()
    diagnose = models.ForeignKey(
        "diagnosis.Diagnose",
        related_name="queries",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.prompt

    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = "Queries"
