from django.db import models
from core.models import BaseModel


class Service(BaseModel):
    title = models.CharField(max_length=150)

    slug = models.SlugField(
        unique=True,
        blank=True
    )
    short_description = models.TextField()
    full_description = models.TextField(blank=True,default="")
    image = models.ImageField(
        upload_to="company/services/"
    )
    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Bootstrap Icon Class (Example: bi bi-cpu)"
    )
    is_featured = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=1)
    class Meta:
        ordering = ["display_order"]
        verbose_name = "Service"
        verbose_name_plural = "Services"
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        from core.utils import generate_unique_slug
        if not self.slug:
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)