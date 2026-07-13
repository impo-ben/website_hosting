from django.db import models

from core.models import BaseModel


class HeroBanner(BaseModel):
    title = models.CharField(max_length=200)

    subtitle = models.CharField(
        max_length=300,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    desktop_image = models.ImageField(
        upload_to="company/hero/"
    )

    mobile_image = models.ImageField(
        upload_to="company/hero/mobile/",
        blank=True,
        null=True
    )

    button_one_text = models.CharField(
        max_length=50,
        blank=True
    )

    button_one_url = models.CharField(
        max_length=255,
        blank=True
    )

    button_two_text = models.CharField(
        max_length=50,
        blank=True
    )

    button_two_url = models.CharField(
        max_length=255,
        blank=True
    )

    overlay_opacity = models.PositiveSmallIntegerField(
        default=50
    )

    display_order = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Hero Banner"
        verbose_name_plural = "Hero Banners"

    def __str__(self):
        return self.title

'''class AboutCompany(BaseModel):

    company_name = models.CharField(max_length=200)

    heading = models.CharField(max_length=250)

    sub_heading = models.CharField(
        max_length=300,
        blank=True
    )

    short_description = models.TextField()

    full_description = models.TextField()

    image = models.ImageField(
        upload_to="company/about/"
    )

    mission = models.TextField()

    vision = models.TextField()

    experience_years = models.PositiveIntegerField(default=1)

    happy_clients = models.PositiveIntegerField(default=0)

    completed_projects = models.PositiveIntegerField(default=0)

    engineers = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "About Company"
        verbose_name_plural = "About Company"

    def __str__(self):
        return self.company_name'''   
class AboutCompany(BaseModel):
    company_name = models.CharField(max_length=200)

    title = models.CharField(max_length=250)

    short_description = models.TextField()

    full_description = models.TextField()

    image = models.ImageField(
        upload_to="company/about/"
    )

    mission = models.TextField()

    vision = models.TextField()

    experience_years = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        verbose_name = "About Company"
        verbose_name_plural = "About Company"

    def __str__(self):
        return self.company_name
    
class WhyChooseUs(BaseModel):
    title = models.CharField(max_length=100)

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        help_text="Bootstrap Icon class, e.g. bi bi-robot"
    )

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Why Choose Us"
        verbose_name_plural = "Why Choose Us"

    def __str__(self):
        return self.title
    
class Service(BaseModel):
    title = models.CharField(max_length=150)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    short_description = models.TextField()

    image = models.ImageField(
        upload_to="company/services/"
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Bootstrap Icon class"
    )

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        from core.utils import generate_unique_slug

        if not self.slug:
            self.slug = generate_unique_slug(self, self.title)

        super().save(*args, **kwargs)
        
class Achievement(BaseModel):
    title = models.CharField(max_length=100)

    value = models.PositiveIntegerField()

    suffix = models.CharField(
        max_length=5,
        default="+",
        help_text="Examples: +, %, Years"
    )

    icon = models.CharField(
        max_length=100,
        blank=True
    )

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.title

           
class Partner(BaseModel):

    name = models.CharField(max_length=150)

    logo = models.ImageField(
        upload_to="company/partners/"
    )

    website = models.URLField(blank=True)

    partnership_type = models.CharField(
        max_length=100,
        blank=True
    )

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.name
    
class Testimonial(BaseModel):
    client_name = models.CharField(max_length=100)

    company = models.CharField(
        max_length=150,
        blank=True
    )

    designation = models.CharField(
        max_length=150,
        blank=True
    )

    photo = models.ImageField(
        upload_to="company/testimonials/"
    )

    review = models.TextField()

    rating = models.PositiveSmallIntegerField(default=5)

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.client_name
    
class ContactInfo(BaseModel):
    company_name = models.CharField(max_length=200)

    address = models.TextField()

    phone = models.CharField(max_length=30)

    email = models.EmailField()

    google_map = models.TextField(
        blank=True
    )

    working_hours = models.CharField(
        max_length=200,
        blank=True
    )

    def __str__(self):
        return self.company_name
    
class SocialLink(BaseModel):
    platform = models.CharField(max_length=50)

    icon = models.CharField(
        max_length=100,
        help_text="Bootstrap Icon class"
    )

    url = models.URLField()

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.platform
    
class SEOSetting(BaseModel):
    page_name = models.CharField(max_length=100)

    meta_title = models.CharField(max_length=255)

    meta_description = models.TextField()

    meta_keywords = models.TextField(
        blank=True
    )

    og_image = models.ImageField(
        upload_to="company/seo/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.page_name