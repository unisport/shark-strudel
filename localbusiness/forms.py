from django import forms

from .models import LocalBusiness, OpeningHours


class LocalBusinessForm(forms.ModelForm):
    class Meta:
        model = LocalBusiness
        fields = ['site_id', 'name', 'streetAddress', 'addressLocality',
                    'addressRegion', 'postalCode', 'addressCountry', 'telephone',
                    'additional_text']
        fields_required = ['site_id', 'name']
        widgets = {'additional_text': forms.Textarea()}
