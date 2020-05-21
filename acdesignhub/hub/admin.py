from django.contrib import admin, messages

from django.utils.html import mark_safe

from django.urls import path, reverse

from django.http import HttpResponseRedirect

from .models import Design, Image

class DesignImagesInline(admin.StackedInline):
    model = Image

    extra = 0

    fields = (
        'image_preview',
        'image',
    )

    readonly_fields = (
        'image_preview',
    )

    def image_preview(self, image):
        return mark_safe(f"""
            <a href="{image.image.url}">
                <img style="width: auto; max-width: 100%" src="{image.image.url}" />
            </a>
        """)

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

    inlines = (DesignImagesInline, )

    list_display = (
        'design_name',
        'design_code_formatted',
        'creator_info',
        'design_thumbnail',
        'image_dimensions',
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

    def design_code_formatted(self, design):
        return mark_safe(f"""
            <span style="font-family:monospace; letter-spacing:2px;">
                {design.design_code}
            </span>
        """)
    design_code_formatted.admin_order_field = 'design_code'

    def creator_info(self, design):
        return mark_safe(f"""
            <dl>
                <dt>Creator Code<dt>
                <dd style="font-family:monospace; letter-spacing:2px;">
                    {design.creator_code}
                </dd>
                <dt>Creator Name</dt>
                <dd>{design.creator_name}</dd>
                <dt>Creator Island</dt>
                <dd>{design.creator_island}</dd>
            </dl>
        """)
    creator_info.admin_order_field = 'creator_code'

    def approval_actions(self, design):
        icon = "yes" if design.approved else "no"
        action = "unapprove" if design.approved else "approve"

        view_link = ''
        if design.approved:
            view_link = mark_safe(f"""
                <a style="padding:6px 8px; background:#eee; border-radius:3px; margin-left: .5rem;" href="/design/{design.design_code}" title="view">View</a>
            """)

        return mark_safe(f"""
            <a style="padding:6px 8px; background:#eee; border-radius:3px" href="{design.id}/{action}" title="{action}">
                <img style="width:20px;" src="/static/admin/img/icon-{icon}.svg" alt="True">
            </a>
            {view_link}
        """)

    def design_thumbnail(self, design):
        return mark_safe(f"""
            <a href="{design.original_image.url}">
                <img style="max-height: 10rem;" src="{design.original_image.url}" />
            </a>
        """)

    def image_dimensions(self, design):
        rec_width = 1280
        rec_height = 720

        width = design.original_image.width
        height = design.original_image.height

        paragraph_style = ''
        if width < .75 * rec_width or height < .75 * rec_height:
            paragraph_style = 'background: red;'
        elif width < rec_width or height < rec_height:
            paragraph_style = 'background: yellow;'

        return mark_safe(f"""
            <p style="{paragraph_style}">
                {width} x {height}
            <p>
        """)


    def design_preview(self, design):
        return mark_safe(f"""
            <a href="{design.original_image.url}">
                <img style="width: auto; max-width: 100%" src="{design.original_image.url}" />
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
