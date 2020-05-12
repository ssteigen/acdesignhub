from django.contrib import admin

from .models import Design

@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):

    list_display = (
        'design_name',
        'creator_code',
        'design_code',
        'original_image',
        'view_count',
        'download_count',
        'approved',
    )

    actions = (
        'approve',
        'unapprove',
    )

    def approve(self, request, designs, *args, **kwargs):
        """Approves a design."""
        designs.update(approved=True)

    def unapprove(self, request, designs, *args, **kwargs):
        """Un-approves a design."""
        designs.update(approved=False)
