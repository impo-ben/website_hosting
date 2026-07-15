from django.db import models

from django.conf import settings

from core.models import BaseModel

from .product import Product


class Cart(BaseModel):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cart_items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        unique_together = ("user", "product")

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.user} - {self.product.name}"