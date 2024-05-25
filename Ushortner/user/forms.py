# forms.py
from django import forms
from urlshortner.models import ShortURL
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomShortURLForm(forms.ModelForm):
    custom_short_code = forms.CharField(
        max_length=20, 
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter custom short code here',
            'class': "p-2.5 text-md text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        })
        )

    class Meta:
        model = ShortURL
        fields = ['original_url']
        widgets = {
            'original_url': forms.URLInput(attrs={
                'placeholder': 'Enter URL here',
                'class': "p-2.5 text-md text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            })
        }

class GenerateQRCodeForm(forms.Form):
    url = forms.URLField(label='Enter URL', widget=forms.URLInput(attrs={
        'placeholder': 'Enter URL here',
        'class':"p-2.5 text-md text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",

        }))


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # field.widget.attrs['class'] = ' p-2.5 dark:bg-gray-sm-light'
            field.widget.attrs['placeholder'] = field.label
