from django.contrib import admin

from .models import (
    HeroBanner,
    AboutCompany,
    WhyChooseUs,
    Achievement,
    Partner,
    Testimonial,
    ContactInfo,
    SocialLink,
    SEOSetting,
    ContactMessage,

)

class SingletonAdmin(admin.ModelAdmin):
    """
    Prevent more than one instance of a model.
    """

    def has_add_permission(self, request):
        return self.model.objects.count() < 1

@admin.register(HeroBanner)
class HeroBannerAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "display_order",
        "is_active",
        "created_at",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    search_fields = (
        "title",
        "subtitle",
    )

    ordering = (
        "display_order",
    )
    
@admin.register(AboutCompany)
class AboutCompanyAdmin(SingletonAdmin):

    list_display = (
        "company_name",
        "experience_years",
        "is_active",
    )
    
@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "display_order",
        "is_active",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
    )

    search_fields = (
        "title",
    )
    
# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):

#     list_display = (
#         "title",
#         "display_order",
#         "is_active",
#     )

#     list_editable = (
#         "display_order",
#         "is_active",
#     )

#     prepopulated_fields = {
#         "slug": ("title",)
#     }

#     search_fields = (
#         "title",
#     )

#     ordering = (
#         "display_order",
#     )

# @admin.register(ServiceInquiry)
# class ServiceInquiryAdmin(admin.ModelAdmin):

#     list_display = (
#         "full_name",
#         "service",
#         "phone",
#         "email",
#         "status",
#         "created_at",
#     )

#     list_filter = (
#         "status",
#         "service",
#     )

#     search_fields = (
#         "full_name",
#         "email",
#         "phone",
#     )

#     list_editable = (
#         "status",
#     )

#     ordering = (
#         "-created_at",
#     )
    
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "value",
        "suffix",
        "display_order",
        "is_active",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    search_fields = (
        "title",
    )

    ordering = (
        "display_order",
    )
    
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "display_order",
        "is_active",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
    )

    search_fields = (
        "name",
    )
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        "client_name",
        "company",
        "rating",
        "display_order",
        "is_active",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
    )

    search_fields = (
        "client_name",
        "company",
    )
    
@admin.register(ContactInfo)
class ContactInfoAdmin(SingletonAdmin):

    list_display = (
        "company_name",
        "phone",
        "email",
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "email",
        "phone",
        "subject",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
    )

    list_editable = (
        "status",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):

    list_display = (
        "platform",
        "display_order",
        "is_active",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
    )
    
@admin.register(SEOSetting)
class SEOSettingAdmin(SingletonAdmin):

    list_display = (
        "page_name",
        "meta_title",
    )