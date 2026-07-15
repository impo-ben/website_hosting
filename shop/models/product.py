from django.db import models
from core.models import BaseModel
from shop.models import Category

class Product(BaseModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(
        upload_to="shop/products/"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    old_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    stock = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=100)
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=5
    )
    featured = models.BooleanField(default=False)
    def __str__(self):
        return self.name