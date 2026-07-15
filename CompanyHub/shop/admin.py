from django.contrib import admin

from .models import (
    Category,
    Product,
    ProductImage,
    Cart,
    Wishlist,
    Order,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "is_active",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "price",
        "stock",
        "featured",
        "is_active",
    )

    list_filter = (
        "category",
        "featured",
    )

    search_fields = (
        "name",
        "sku",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "display_order",
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "product",
        "quantity",
        "total_price",
    )


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "product",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "total_amount",
        "status",
        "payment_status",
        "created_at",
    )

    list_filter = (
        "status",
        "payment_status",
    )