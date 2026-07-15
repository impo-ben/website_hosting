from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand

from company.models import (
    AboutCompany,
    HeroBanner,
    Partner,
    SEOSetting,
    Testimonial,
)

from portfolio.models import (
    Project,
    ProjectImage,
)
from services.models import Service

from shop.models import (
    Category,
    Product,
    ProductImage,
)


class Command(BaseCommand):
    help = "Upload existing media files to Cloudinary"

    def handle(self, *args, **options):

        models = [

            (AboutCompany, ["image"]),

            (HeroBanner, ["desktop_image", "mobile_image"]),

            (Partner, ["logo"]),

            (SEOSetting, ["og_image"]),

            (Testimonial, ["photo"]),

            (Service, ["image"]),

            (Project, ["featured_image"]),

            (ProjectImage, ["image"]),

            (Category, ["image"]),

            (Product, ["image"]),

            (ProductImage, ["image"]),

        ]

        migrated = 0
        skipped = 0
        failed = 0

        for model, fields in models:

            self.stdout.write(f"\nProcessing {model.__name__}")

            for obj in model.objects.all():

                for field_name in fields:

                    field = getattr(obj, field_name)

                    if not field:
                        continue

                    if field.name.startswith("http"):
                        skipped += 1
                        continue

                    local_file = Path(settings.MEDIA_ROOT) / field.name

                    if not local_file.exists():

                        self.stdout.write(
                            self.style.WARNING(
                                f"Missing: {local_file}"
                            )
                        )
                        failed += 1
                        continue

                    try:

                        with open(local_file, "rb") as f:

                            field.save(
                                local_file.name,
                                File(f),
                                save=False,
                            )

                        obj.save(update_fields=[field_name])

                        migrated += 1

                        self.stdout.write(
                            self.style.SUCCESS(
                                f"✓ {field.name}"
                            )
                        )

                    except Exception as e:

                        failed += 1

                        self.stdout.write(
                            self.style.ERROR(
                                f"✗ {field.name} -> {e}"
                            )
                        )

        self.stdout.write("\n=========================")
        self.stdout.write(f"Migrated : {migrated}")
        self.stdout.write(f"Skipped  : {skipped}")
        self.stdout.write(f"Failed   : {failed}")
        self.stdout.write("=========================")