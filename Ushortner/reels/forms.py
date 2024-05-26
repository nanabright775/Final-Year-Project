from django import forms
from .models import Reel

class ReelForm(forms.ModelForm):
    class Meta:
        model = Reel
        fields = ['video', 'description', 'url',]
        widgets = {
            'video': forms.ClearableFileInput(attrs={
                'accept': 'video/*',
                'max_length': 30000,
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter description here...',
                'rows': 3,
                'class': 'p-2.5 text-md text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            }),
            'url': forms.URLInput(attrs={
                'placeholder': 'Enter URL here...',
                'class': 'p-2.5 text-md text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            }),  
        }
