from django.db import models
from core.models import BaseModel


class WhyChooseUs(BaseModel):

    title = models.CharField(max_length=100)

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        help_text="Bootstrap Icon class, e.g. bi bi-robot"
    )

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Why Choose Us"
        verbose_name_plural = "Why Choose Us"

    def __str__(self):
        return self.title