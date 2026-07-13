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


class Project(BaseModel):
    category = models.ForeignKey(
        PortfolioCategory,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    short_description = models.TextField()

    full_description = models.TextField()

    featured_image = models.ImageField(
        upload_to="portfolio/projects/"
    )

    client = models.CharField(
        max_length=200,
        blank=True
    )

    project_date = models.DateField()

    location = models.CharField(
        max_length=150,
        blank=True
    )

    technologies = models.ManyToManyField(
        Technology,
        blank=True,
        related_name="projects"
    )

    is_featured = models.BooleanField(default=False)

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)


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