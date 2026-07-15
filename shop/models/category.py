from django.db import models
from core.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        upload_to="shop/categories/",
        blank=True,
        null=True
    )
    def __str__(self):
        return self.name