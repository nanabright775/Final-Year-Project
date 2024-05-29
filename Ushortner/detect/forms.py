# detect/forms.py

from django import forms

class URLForm(forms.Form):
    url = forms.URLField(
        label='URL',
        widget=forms.URLInput(attrs={
            'class': 'w-full mt-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50',
            'placeholder': 'Enter a URL to check'
        })
    )
