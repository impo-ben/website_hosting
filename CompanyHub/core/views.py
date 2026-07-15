from django.shortcuts import render

from services.forms import ServiceInquiryForm

from company.models import (
    HeroBanner,
    AboutCompany,
    WhyChooseUs,
    Achievement,
    Testimonial,
    Partner,
    ContactInfo,
    SocialLink,
    
)

from portfolio.models import Project
from shop.models import Product
from services.models import Service
from company.forms import ContactMessageForm

contact_form = ContactMessageForm()
def home(request):

    context = {
        "hero_banners": HeroBanner.objects.filter(is_active=True),

        "about": AboutCompany.objects.filter(is_active=True).first(),

        "why_choose_us": WhyChooseUs.objects.filter(is_active=True),

        "services": Service.objects.filter(
            is_active=True,
            is_featured=True
        ),

        "achievements": Achievement.objects.filter(is_active=True),

        "featured_projects": Project.objects.filter(
            is_active=True,
            is_featured=True
        ).select_related(
            "category"
        ).prefetch_related(
            "technologies"
        )[:6],

        "testimonials": Testimonial.objects.filter(
            is_active=True,
            is_featured=True
        ),
        
        "featured_products": Product.objects.filter(
            is_active=True,
            featured=True
        )[:4],

        "partners": Partner.objects.filter(is_active=True),

        "contact": ContactInfo.objects.filter(is_active=True).first(),
        "contact_form": contact_form,

        "social_links": SocialLink.objects.filter(is_active=True),

        "inquiry_form": ServiceInquiryForm(),
    }

    return render(request, "home/index.html", context)