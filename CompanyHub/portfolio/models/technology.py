from django.db import models
from core.models import BaseModel
from core.utils import generate_unique_slug


class Technology(BaseModel):
    name = models.CharField(max_length=100)
    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Bootstrap Icon class"
    )
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name