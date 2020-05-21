import re

from django import forms

from .models import Design, Image

class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = (
            'original_image',
            'design_name',
            'design_type',
            'design_code',
            'description',
            'creator_name',
            'creator_island',
            'creator_code',
        )
        widgets = {
            'original_image': forms.FileInput(),
            'description': forms.Textarea(attrs={'rows': 2}),
            'design_code': forms.TextInput(attrs={'class': 'text-monospace text-space-out'}),
            'creator_code': forms.TextInput(attrs={'class': 'text-monospace text-space-out'}),
        }

    # Design code regex MO(-[0-9ABCDEFGHJKLMNPQRSTUVWXY]{4}){3}
    def clean_design_code(self):
        design_code = self.cleaned_data['design_code']
        if re.match('MO(-[0-9ABCDEFGHJKLMNPQRSTUVWXY]{4}){3}', design_code):
            return design_code

    # Creator code regex MA(-[0-9]{4}){3}
    def clean_creator_code(self):
        creator_code = self.cleaned_data['creator_code']
        if re.match('MA(-[0-9]{4}){3}', creator_code):
            return creator_code

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Image
        fields = (
            'image',
        )
