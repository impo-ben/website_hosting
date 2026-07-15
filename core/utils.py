from django.utils.text import slugify


def generate_unique_slug(instance, value):
    """
    Generate a unique slug for a model instance.
    """

    slug = slugify(value)
    model = instance.__class__

    unique_slug = slug
    counter = 1

    while model.objects.filter(slug=unique_slug).exclude(pk=instance.pk).exists():
        unique_slug = f"{slug}-{counter}"
        counter += 1

    return unique_slug