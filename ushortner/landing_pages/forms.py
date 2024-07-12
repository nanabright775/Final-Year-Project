# landing_pages/forms.py
from django import forms
from .models import LandingPage

class LandingPageForm(forms.ModelForm):
    class Meta:
        model = LandingPage
        fields = [
            'title', 'description',  'profile_image', 'theme', 'layout', 
            'background_color', 'background_image', 'text_color', 'font_style', 
            'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url',
            'additional_image_1', 'additional_image_2', 'additional_image_3', 'video','name', 'location',
            'welMessage', 'bussiness_name', 'contact',
     
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'theme': forms.RadioSelect(attrs={'class': 'flex flex-row'}),
            'layout': forms.RadioSelect(attrs={'class': 'flex flex-row'}),
            'background_color': forms.TextInput(attrs={'type': 'color', 'class': 'w-full p-2 border border-gray-300 rounded'}),
            'background_image': forms.ClearableFileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'text_color': forms.TextInput(attrs={'type': 'color', 'class': 'w-full p-2 border border-gray-300 rounded'}),
            'font_style': forms.RadioSelect(attrs={'class': 'flex flex-row'}),
            'facebook_url': forms.URLInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'twitter_url': forms.URLInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'instagram_url': forms.URLInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'additional_image1':forms.ClearableFileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'additional_image2':forms.ClearableFileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'additional_image3':forms.ClearableFileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'video':forms.ClearableFileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'location': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'welMessage': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'bussiness_name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'contact': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
        }
