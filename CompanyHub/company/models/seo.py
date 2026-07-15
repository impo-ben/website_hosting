from django.db import models
from core.models import BaseModel


class SEOSetting(BaseModel):

    page_name = models.CharField(max_length=100)

    meta_title = models.CharField(max_length=255)

    meta_description = models.TextField()

    meta_keywords = models.TextField(blank=True)

    og_image = models.ImageField(
        upload_to="company/seo/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.page_name