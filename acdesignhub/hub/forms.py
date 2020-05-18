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

    # Design code regex MA-[0-9]{4}-[0-9]{4}-[0-9]{4}
    def clean_design_code(self):
        design_code = self.cleaned_data['design_code']
        design_code = re.sub('[^0-9AM]+', '', design_code.upper())
        return design_code

    # Creator code regex MO-[0-9ABCDEFGHJKLMNPQRSTUVWXY]{4}-[0-9ABCDEFGHJKLMNPQRSTUVWXY]{4}-[0-9ABCDEFGHJKLMNPQRSTUVWXY]{4}
    def clean_creator_code(self):
        creator_code = self.cleaned_data['creator_code']
        creator_code = re.sub('[^0-9ABCDEFGHJKLMNPQRSTUVWXY]+', '', creator_code.upper())
        return creator_code


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Image
        fields = (
            'image',
        )
