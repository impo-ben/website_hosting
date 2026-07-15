from django.db import models
from core.models import BaseModel


class Partner(BaseModel):

    name = models.CharField(max_length=150)

    logo = models.ImageField(
        upload_to="company/partners/"
    )

    website = models.URLField(blank=True)

    partnership_type = models.CharField(
        max_length=100,
        blank=True
    )

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.name