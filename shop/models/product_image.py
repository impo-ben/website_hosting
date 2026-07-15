from django.db import models

from core.models import BaseModel
from .product import Product


class ProductImage(BaseModel):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="gallery"
    )

    image = models.ImageField(
        upload_to="shop/products/gallery/"
    )

    alt_text = models.CharField(
        max_length=150,
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return f"{self.product.name} Image"