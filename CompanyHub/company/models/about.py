from django.db import models
from core.models import BaseModel


class AboutCompany(BaseModel):

    company_name = models.CharField(max_length=200)

    title = models.CharField(max_length=250)

    short_description = models.TextField()

    full_description = models.TextField()

    image = models.ImageField(
        upload_to="company/about/"
    )

    mission = models.TextField()

    vision = models.TextField()

    experience_years = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "About Company"
        verbose_name_plural = "About Company"

    def __str__(self):
        return self.company_name