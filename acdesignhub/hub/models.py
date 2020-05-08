import time

from django.db import models


def _upload_path(instance: 'Submission', filename: str) -> str:
    """Generates a file path for a design image upload.

    Ensures uniqueness across uploads.
    """
    return f'designs/{int(time.time())}/original-{filename}'


class DesignManager(models.Manager):
    """Manages access to the Design records."""

    def approved(self):
        """Filters only for approved designs."""
        return self.filter(approved=True)


class Design(models.Model):
    """A user-uploaded custom design.

    Stores a reference to the uploaded image along with metadata about the
    design (the design itself, the user it belongs to, etc).
    """

    objects = DesignManager()

    TYPE_CHOICES = (
        ('BALLOON_HEM_DRESS', 'Balloon-hem dress'),
        ('BRIMMED_CAP', 'Brimmed cap'),
        ('BRIMMED_HAT', 'Brimmed hat'),
        ('COAT', 'Coat'),
        ('CUSTOM_DESIGN', 'Custom design'),
        ('HOODIE', 'Hoodie'),
        ('KNIT_CAP', 'Knit cap'),
        ('LONG_SLEEVE_DRESS', 'Long-sleeve dress'),
        ('LONG_SLEEVE_DRESS_SHIRT', 'Long-sleeve dress shirt'),
        ('ROBE', 'Robe'),
        ('ROUND_DRESS', 'Round dress'),
        ('SHORT_SLEEVE_DRESS', 'Short-sleeve dress'),
        ('SHORT_SLEEVE_TEE', 'Short-sleeve tee'),
        ('SLEEVELESS_DRESS', 'Sleeveless dress'),
        ('SWEATER', 'Sweater'),
        ('TANK_TOP', 'Tank top'),
    )

    # The original uploaded image.
    original_image = models.FileField(upload_to=_upload_path, max_length=1024)

    # Design metadata.
    design_name = models.CharField(max_length=255)
    design_type = models.CharField(choices=TYPE_CHOICES, max_length=128)
    design_code = models.CharField(max_length=17)
    description = models.TextField(blank=True, null=True)

    # Creator metadata.
    creator = models.CharField(max_length=10)
    creator_code = models.CharField(max_length=17)

    # Administration
    approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.design_name} ({self.creator})'
