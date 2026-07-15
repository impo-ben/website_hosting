from django.shortcuts import redirect
from django.contrib import messages
from .models import Service
from django.shortcuts import render, get_object_or_404
from .forms import ServiceInquiryForm
from company.models import ContactInfo
from services.models import Service


def service_inquiry(request):

    if request.method == "POST":

        form = ServiceInquiryForm(request.POST)

        if form.is_valid():

            inquiry = form.save(commit=False)

            inquiry.service_id = request.POST.get("service")

            inquiry.save()

            messages.success(
                request,
                "Your enquiry has been submitted successfully."
            )

        else:

            print(form.errors)

            messages.error(
                request,
                "Please correct the errors in the form."
            )

    return redirect("home")

def service_detail(request, slug):

    service = get_object_or_404(
        Service,
        slug=slug,
        is_active=True
    )

    related_services = Service.objects.filter(
        is_active=True
    ).exclude(
        id=service.id
    )[:3]

    inquiry_form = ServiceInquiryForm()

    context = {

        "service": service,

        "related_services": related_services,

        "contact": ContactInfo.objects.filter(
            is_active=True
        ).first(),

        "inquiry_form": inquiry_form,
        "services": Service.objects.filter(
        is_active=True
    ),

    "contact": ContactInfo.objects.filter(
        is_active=True
    ).first(),

    # "social_links": SocialLink.objects.filter(
    #     is_active=True
    # ),

    }

    return render(
        request,
        "services/detail.html",
        context,
    )