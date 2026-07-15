from django.db import models


class BaseModel(models.Model):
    """
    Base model inherited by all application models.
    """

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True