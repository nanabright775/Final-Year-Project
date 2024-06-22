from django import forms
from .models import UserProfile, Portfolio

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'bio', 'cv']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'block w-full px-4 py-2 mt-2 border rounded-md focus:border-blue-400 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40'}),
            'email': forms.EmailInput(attrs={'class': 'block w-full px-4 py-2 mt-2 border rounded-md focus:border-blue-400 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40'}),
            'bio': forms.Textarea(attrs={'class': 'block w-full px-4 py-2 mt-2 border rounded-md focus:border-blue-400 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40'}),
            'cv': forms.FileInput(attrs={'class': 'block w-full px-4 py-2 mt-2 border rounded-md focus:border-blue-400 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40'}),
        }

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'block w-full px-4 py-2 mt-2 border rounded-md focus:border-blue-400 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40'}),
            'content': forms.Textarea(attrs={'class': 'block w-full px-4 py-2 mt-2 border rounded-md focus:border-blue-400 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40'}),
        }

