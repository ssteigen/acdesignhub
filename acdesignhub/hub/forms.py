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
            'designer',
            'designer_code',
        )
