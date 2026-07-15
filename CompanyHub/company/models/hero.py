from django.db import models
from core.models import BaseModel


class HeroBanner(BaseModel):
    title = models.CharField(max_length=200)

    subtitle = models.CharField(
        max_length=300,
        blank=True
    )

    description = models.TextField(blank=True)

    desktop_image = models.ImageField(
        upload_to="company/hero/"
    )

    mobile_image = models.ImageField(
        upload_to="company/hero/mobile/",
        blank=True,
        null=True
    )

    button_one_text = models.CharField(
        max_length=50,
        blank=True
    )

    button_one_url = models.CharField(
        max_length=255,
        blank=True
    )

    button_two_text = models.CharField(
        max_length=50,
        blank=True
    )

    button_two_url = models.CharField(
        max_length=255,
        blank=True
    )

    overlay_opacity = models.PositiveSmallIntegerField(default=50)

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Hero Banner"
        verbose_name_plural = "Hero Banners"

    def __str__(self):
        return self.title