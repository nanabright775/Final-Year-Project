# forms.py
from django import forms
from urlshortner.models import ShortURL
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomShortURLForm(forms.ModelForm):
    custom_short_code = forms.CharField(max_length=20, required=True)

    class Meta:
        model = ShortURL
        fields = ['original_url']


class GenerateQRCodeForm(forms.Form):
    url = forms.URLField(label='Enter URL', widget=forms.URLInput(attrs={'placeholder': 'Enter URL here'}))


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # field.widget.attrs['class'] = ' p-2.5 dark:bg-gray-sm-light'
            field.widget.attrs['placeholder'] = field.label
