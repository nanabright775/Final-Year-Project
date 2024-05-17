# forms.py
from django import forms
from urlshortner.models import ShortURL

class CustomShortURLForm(forms.ModelForm):
    custom_short_code = forms.CharField(max_length=20, required=True)

    class Meta:
        model = ShortURL
        fields = ['original_url']


class GenerateQRCodeForm(forms.Form):
    url = forms.URLField(label='Enter URL', widget=forms.URLInput(attrs={'placeholder': 'Enter URL here'}))
