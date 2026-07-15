from company.models import (
    HeroBanner,
    AboutCompany,
    WhyChooseUs,
    Achievement,
    Partner,
    ContactInfo,
    SocialLink,
    Testimonial,
)
from django.shortcuts import redirect
from django.contrib import messages

from .forms import ContactMessageForm


def contact_message(request):

    if request.method == "POST":

        form = ContactMessageForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Thank you! We received your message."
            )

        else:

            messages.error(
                request,
                "Please check the form and try again."
            )

    return redirect("home")