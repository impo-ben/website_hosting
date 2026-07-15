from django.db import models
from core.models import BaseModel
from services.models import Service


class ServiceInquiry(BaseModel):
    STATUS = (
        ("new", "New"),
        ("contacted", "Contacted"),
        ("quoted", "Quotation Sent"),
        ("closed", "Closed"),
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="inquiries"
    )
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(
        max_length=150,
        blank=True
    )
    message = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="new"
    )
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Service Inquiry"
        verbose_name_plural = "Service Inquiries"
    def __str__(self):
        return f"{self.full_name} - {self.service.title}"