from django.db import models
from core.models import BaseModel

class Testimonial(BaseModel):
    client_name = models.CharField(max_length=100)
    company = models.CharField(
        max_length=150,
        blank=True
    )
    designation = models.CharField(
        max_length=150,
        blank=True
    )
    photo = models.ImageField(
        upload_to="company/testimonials/"
    )
    review = models.TextField()
    rating = models.PositiveSmallIntegerField(
        default=5
    )
    display_order = models.PositiveIntegerField(
        default=1
    )
    is_featured = models.BooleanField(
        default=True
    )
    class Meta:
        ordering = ["display_order"]
    def __str__(self):
        return self.client_name