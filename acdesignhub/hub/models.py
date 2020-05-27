import time
import pathlib

from django.db import models
from django.db.models import Q
from django.db.models.functions import Concat

def _design_upload_path(instance: 'Submission', filename: str) -> str:
    """Generates a file path for a design image upload.
    """

    return f'designs/{instance.design_code}{pathlib.Path(filename).suffix}'

def _upload_path(instance: 'Submission', filename: str) -> str:
    """Generates a file path for an image upload.

    Ensures uniqueness across uploads.
    """
    return f'images/{int(time.time())}/original-{filename}'

class DesignManager(models.Manager):
    """Manages access to the Design records."""

    def approved(self):
        """Filters only for approved designs."""
        return self.filter(approved=True)

    def approved_hats(self):
        return self.filter(
            Q(approved=True),
            Q(design_type='BRIMMED_CAP') | Q(design_type='BRIMMED_HAT') | Q(design_type='KNIT_CAP')
        )

class Design(models.Model):
    """A user-uploaded custom design.

    Stores a reference to the uploaded image along with metadata about the
    design (the design itself, the user it belongs to, etc).
    """

    class Meta:
        ordering = ['-created_at']

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
    # undocked FB upload
    # file_size: 69KB
    # file_type: JPEG
    # image_width: 1280
    # image_height: 720
    original_image = models.ImageField(upload_to=_design_upload_path, max_length=1024)

    # Design metadata.
    design_name = models.CharField(max_length=20)
    design_type = models.CharField(choices=TYPE_CHOICES, max_length=128)
    design_code = models.CharField(max_length=17)
    description = models.TextField(blank=True, null=True)
    view_count = models.IntegerField(default=0)
    download_count = models.IntegerField(default=0)

    # Creator metadata.
    creator_name = models.CharField(max_length=10)
    creator_island = models.CharField(max_length=10)
    creator_code = models.CharField(max_length=17)

    # Administration
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.design_name} ({self.creator_name})'

class Image(models.Model):
    design = models.ForeignKey(
        Design,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to=_upload_path)
