from django.shortcuts import render, get_object_or_404

from .models.product import Product


def shop_home(request):

    products = Product.objects.filter(
        is_active=True
    ).select_related("category")

    return render(
        request,
        "shop/shop.html",
        {
            "products": products
        }
    )


def product_detail(request, slug):

    product = get_object_or_404(
        Product,
        slug=slug,
        is_active=True
    )

    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(
        id=product.id
    )[:4]

    return render(
        request,
        "shop/product_detail.html",
        {
            "product": product,
            "related_products": related_products,
        }
    )