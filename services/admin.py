from django.contrib import admin

# Register your models here.
from services.models import (
    Service,
    ServiceInquiry,
)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "display_order",
        "is_active",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    search_fields = (
        "title",
    )

    ordering = (
        "display_order",
    )

@admin.register(ServiceInquiry)
class ServiceInquiryAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "service",
        "phone",
        "email",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "service",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
    )

    list_editable = (
        "status",
    )

    ordering = (
        "-created_at",
    )
    