from django import forms
from .models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['url', 'description', 'image']
