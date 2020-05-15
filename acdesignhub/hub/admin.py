from django.contrib import admin, messages

from django.utils.html import mark_safe

from django.urls import path, reverse

from django.http import HttpResponseRedirect

from .models import Design

@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Image Info', {
            'fields': (
                'design_preview',
                'original_image',
            )
        }),
        ('Design Info', {
            'fields': (
                'design_name',
                'design_code',
            )
        }),
        ('Creator Info', {
            'fields': (
                'creator_name',
                'creator_island',
                'creator_code',
            )
        }),
        ('Stats', {
            'fields': (
                'view_count',
                'download_count',
            )
        }),
        ('Actions', {
            'fields': (
                'approved',
            )
        }),
    )

    list_display = (
        'design_name',
        'creator_code',
        'design_code',
        'design_thumbnail',
        'view_count',
        'download_count',
        'created_at',
        'approval_actions',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'design_preview',
        'design_thumbnail',
        'view_count',
        'download_count',
    )

    actions = (
        'approve',
        'unapprove',
    )

    def approval_actions(self, design):
        icon = "yes" if design.approved else "no"
        action = "unapprove" if design.approved else "approve"

        return mark_safe(f"""
            <a style="padding:6px 8px; background:#eee; border-radius:3px" href="{design.id}/{action}" title="{action}">
                <img style="width:20px;" src="/static/admin/img/icon-{icon}.svg" alt="True">
            </a>
        """)

    def design_thumbnail(self, design):
        return mark_safe(f"""
            <a href="{design.original_image.url}">
                <img style="width: 200px;" src="{design.original_image.url}" />
            </a>
        """)

    def design_preview(self, design):
        return mark_safe(f"""
            <a href="{design.original_image.url}">
                <img style="width: 100%;" src="{design.original_image.url}" />
            </a>
        """)

    def approve(self, request, designs, *args, **kwargs):
        """Approves a design."""
        designs.update(approved=True)

    def unapprove(self, request, designs, *args, **kwargs):
        """Un-approves a design."""
        designs.update(approved=False)

    def approve_design(self, request, design_id, *args, **kwargs):
        self.approve(request, designs=Design.objects.filter(pk=design_id), *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, f'Design {design_id} approved!')
        list_url = reverse('admin:hub_design_changelist')
        return HttpResponseRedirect(list_url)

    def unapprove_design(self, request, design_id, *args, **kwargs):
        self.unapprove(request, designs=Design.objects.filter(pk=design_id), *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, f'Design {design_id} unapproved!')
        list_url = reverse('admin:hub_design_changelist')
        return HttpResponseRedirect(list_url)

    def get_urls(self):
        return [
            path(
                '<int:design_id>/approve/',
                self.admin_site.admin_view(self.approve_design),
                name='approve-design',
            ),
            path(
                '<int:design_id>/unapprove/',
                self.admin_site.admin_view(self.unapprove_design),
                name='unapprove-design',
            ),
            *super().get_urls(),
        ]
