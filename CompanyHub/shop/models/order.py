from django.db import models

from django.conf import settings

from core.models import BaseModel


class Order(BaseModel):

    STATUS = (
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    full_name = models.CharField(
        max_length=150
    )

    phone = models.CharField(
        max_length=20
    )

    email = models.EmailField()

    address = models.TextField()

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=100
    )

    postal_code = models.CharField(
        max_length=20
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="pending"
    )

    payment_status = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"Order #{self.id}"