from django.db import models
from core.models import BaseModel


class ContactInfo(BaseModel):

    company_name = models.CharField(max_length=200)

    address = models.TextField()

    phone = models.CharField(max_length=30)

    whatsapp = models.CharField(
        max_length=30,
        blank=True
    )

    email = models.EmailField()

    google_map = models.TextField(
        blank=True
    )

    working_hours = models.CharField(
        max_length=200,
        blank=True
    )

    support_email = models.EmailField(
        blank=True
    )

    latitude = models.CharField(
        max_length=50,
        blank=True
    )

    longitude = models.CharField(
        max_length=50,
        blank=True
    )

    class Meta:
        verbose_name = "Contact Information"

    def __str__(self):
        return self.company_name
    
    
class ContactMessage(BaseModel):

    STATUS = (
        ("new", "New"),
        ("read", "Read"),
        ("replied", "Replied"),
        ("closed", "Closed"),
    )

    full_name = models.CharField(max_length=150)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    subject = models.CharField(max_length=200)

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="new"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return self.full_name


class SocialLink(BaseModel):
    platform = models.CharField(max_length=50)
    icon = models.CharField(
        max_length=100,
        help_text="Bootstrap Icon class"
    )
    url = models.URLField()
    display_order = models.PositiveIntegerField(default=1)
    class Meta:
        ordering = ["display_order"]
    def __str__(self):
        return self.platform