from django.db import models
from core.models import BaseModel

class Achievement(BaseModel):
    title = models.CharField(max_length=100)
    value = models.PositiveIntegerField()
    suffix = models.CharField(
        max_length=5,
        default="+",
        help_text="Examples: +, %, Years"
    )
    icon = models.CharField(
        max_length=100,
        blank=True
    )
    display_order = models.PositiveIntegerField(default=1)
    class Meta:
        ordering = ["display_order"]
    def __str__(self):
        return self.title