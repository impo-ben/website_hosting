
from django.db import models
from core.models import BaseModel
from core.utils import generate_unique_slug
from portfolio.models import Project

class ProjectImage(BaseModel):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="gallery"
    )
    image = models.ImageField(
        upload_to="portfolio/gallery/"
    )
    caption = models.CharField(
        max_length=150,
        blank=True
    )
    display_order = models.PositiveIntegerField(default=1)
    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return f"{self.project.title} - Image"