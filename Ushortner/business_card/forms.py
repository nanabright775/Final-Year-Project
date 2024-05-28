# business_card/forms.py

from django import forms
from .models import UserBusinessCard


class UserBusinessCardForm(forms.ModelForm):
    class Meta:
        model = UserBusinessCard
        fields = [
            'template', 'name', 'company_name', 'email', 'phone_number', 
            'linkedin', 'twitter', 'facebook', 'instagram'
        ]
        widgets = {
            'template': forms.Select(attrs={
                'class': 'block w-full mt-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            }),
            'name': forms.TextInput(attrs={
                'class': 'block w-full mt-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'block w-full mt-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'block w-full mt-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'block w-full mt-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            }),
            'linkedin': forms.URLInput(attrs={
                'class': 'block w-full mt-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            }),
            'twitter': forms.URLInput(attrs={
                'class': 'block w-full mt-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            }),
            'facebook': forms.URLInput(attrs={
                'class': 'block w-full mt-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            }),
            'instagram': forms.URLInput(attrs={
                'class': 'block w-full mt-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            }),
        }
