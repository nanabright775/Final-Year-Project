from django import forms
from .models import UserBusinessCard

#form for bussiness card creation
class UserBusinessCardForm(forms.ModelForm):
    class Meta:
        model = UserBusinessCard
        fields = [
            'template', 'custom_template_image', 'name', 'company_name', 'email', 'phone_number', 
            'linkedin', 'twitter', 'facebook', 'instagram', 'logo',
        ]
        widgets = {
            'template': forms.Select(attrs={
                'class': 'block w-full mt-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            }),
            'custom_template_image': forms.ClearableFileInput(attrs={
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
            'logo': forms.ClearableFileInput(attrs={'class': 'block w-full mt-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            
            }),
        }
