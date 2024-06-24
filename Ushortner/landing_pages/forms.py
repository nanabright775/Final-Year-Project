# landing_pages/forms.py
from django import forms
from .models import LandingPage

class LandingPageForm(forms.ModelForm):
    class Meta:
        model = LandingPage
        fields = [
            'title', 'description', 'name', 'profile_image', 'theme', 'layout', 
            'background_color', 'background_image', 'text_color', 'font_style', 
            'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'theme': forms.RadioSelect(attrs={'class': 'flex flex-col'}),
            'layout': forms.RadioSelect(attrs={'class': 'flex flex-col'}),
            'background_color': forms.TextInput(attrs={'type': 'color', 'class': 'w-full p-2 border border-gray-300 rounded'}),
            'background_image': forms.ClearableFileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'text_color': forms.TextInput(attrs={'type': 'color', 'class': 'w-full p-2 border border-gray-300 rounded'}),
            'font_style': forms.RadioSelect(attrs={'class': 'flex flex-col'}),
            'facebook_url': forms.URLInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'twitter_url': forms.URLInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'instagram_url': forms.URLInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
        }
