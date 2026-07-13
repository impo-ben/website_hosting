    
from django.shortcuts import render
from portfolio.models import Project

from company.models import (
    HeroBanner,
    AboutCompany,
    WhyChooseUs,
    Service,
    Achievement,
    Testimonial,
    Partner,
    ContactInfo,
    SocialLink,
)

def home(request):

    context = {
        "hero_banners": HeroBanner.objects.filter(is_active=True),
        "about": AboutCompany.objects.filter(is_active=True).first(),
        "why_choose_us": WhyChooseUs.objects.filter(is_active=True),
        "services": Service.objects.filter(is_active=True),
        "achievements": Achievement.objects.filter(is_active=True),
        "testimonials": Testimonial.objects.filter(is_active=True),
        "partners": Partner.objects.filter(is_active=True),
        "contact": ContactInfo.objects.filter(is_active=True).first(),
        "social_links": SocialLink.objects.filter(is_active=True),
        "featured_projects": Project.objects.filter(is_active=True,is_featured=True,).select_related("category").prefetch_related("technologies")[:6],
    }

    return render(request, "home/index.html", context)