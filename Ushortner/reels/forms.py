from django import forms
from .models import Reel

class ReelForm(forms.ModelForm):
    class Meta:
        model = Reel
        fields = ['video', 'description', 'url']
        widgets = {
            'video': forms.ClearableFileInput(attrs={
                'accept': 'video/*',
                'class': 'block w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter description here...',
                'rows': 3,
                'class': 'block w-full p-2.5 text-md text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500',
            }),
            'url': forms.URLInput(attrs={
                'placeholder': 'Enter URL here...',
                'class': 'block w-full p-2.5 text-md text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500',
            }),
        }
