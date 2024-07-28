from django import forms
from .models import Campaign, Reel, Comment

#forms for campaign
class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['url', 'description', 'image']
        widgets = {
            'url': forms.URLInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50'}),
            'description': forms.Textarea(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50', 'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50'}),
        }

#forms for models
class ReelForm(forms.ModelForm):
    class Meta:
        model = Reel
        fields = ['video', 'description', 'url']
        widgets = {
            'video': forms.ClearableFileInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50'}),
            'description': forms.Textarea(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50', 'rows': 4}),
            'url': forms.URLInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50'}),
        }

#forms for comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50', 'rows': 4}),
        }
