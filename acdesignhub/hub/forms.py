import re

from django import forms

from .models import Design

class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = (
            'original_image',
            'design_name',
            'design_type',
            'design_code',
            'description',
            'creator',
            'creator_code',
        )

    def clean_design_code(self):
        design_code = self.cleaned_data['design_code']
        design_code = re.sub('[^0-9A-Z]+', '', design_code.upper())
        return design_code

    def clean_creator_code(self):
        creator_code = self.cleaned_data['creator_code']
        creator_code = re.sub('[^0-9A-Z]+', '', creator_code.upper())
        return creator_code
