from django.db import models
from core.models import BaseModel
from core.utils import generate_unique_slug


class PortfolioCategory(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True,
        blank=True
    )
    description = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=1)
    class Meta:
        ordering = ["display_order"]
        verbose_name = "Portfolio Category"
        verbose_name_plural = "Portfolio Categories"
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.name)
        super().save(*args, **kwargs)