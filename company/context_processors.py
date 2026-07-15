from company.models import ContactInfo, SocialLink
from services.models import Service


def global_data(request):

    contact = ContactInfo.objects.filter(
        is_active=True
    ).first()

    services = Service.objects.filter(
        is_active=True
    )

    social_links = SocialLink.objects.filter(
        is_active=True
    )

    return {

        # New names
        "footer_contact": contact,
        "footer_services": services,
        "footer_social": social_links,

        # Backward-compatible names
        "contact": contact,
        "services": services,
        "social_links": social_links,
    }