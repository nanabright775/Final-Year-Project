from django import forms
from .models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['url', 'description', 'image']
        widgets = {
            'url': forms.URLInput(attrs={
                'class': 'block w-full p-2.5 text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter URL here...',
            }),
            'description': forms.Textarea(attrs={
                'class': 'block w-full p-2.5 text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500',
                'rows': 3,
                'placeholder': 'Enter description here...',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500',
            }),
        }
