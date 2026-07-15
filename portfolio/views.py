from django.shortcuts import render, get_object_or_404

from .models import (
    PortfolioCategory,
    Project,
)


def portfolio(request):

    categories = PortfolioCategory.objects.filter(
        is_active=True
    )

    projects = (
        Project.objects.filter(is_active=True)
        .select_related("category")
        .prefetch_related(
            "technologies",
            "gallery"
        )
    )

    context = {
        "categories": categories,
        "projects": projects,
    }

    return render(
        request,
        "portfolio/index.html",
        context,
    )


def project_detail(request, slug):

    project = get_object_or_404(
        Project.objects.select_related(
            "category"
        ).prefetch_related(
            "technologies",
            "gallery",
        ),
        slug=slug,
        is_active=True,
    )

    context = {
        "project": project,
    }

    return render(
        request,
        "portfolio/detail.html",
        context,
    )