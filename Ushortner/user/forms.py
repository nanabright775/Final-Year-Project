# forms.py
from django import forms
from urlshortner.models import ShortURL
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#forms for a creating a custom shorten url
class CustomShortURLForm(forms.ModelForm):
    custom_short_code = forms.CharField(
        max_length=20, 
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter custom short code here',
            'class': 'block w-full mt-1 p-2 border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50', 'rows': 4}),
              
        )

    class Meta:
        model = ShortURL
        fields = ['original_url']
        widgets = {
            'original_url': forms.URLInput(attrs={
                'placeholder': 'Enter URL here',
                'class': 'block w-full mt-1 p-2 border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50', 'rows': 4}),
          
        }

#forms for generating a qr code
class GenerateQRCodeForm(forms.Form):
    url = forms.URLField(label='Enter URL', widget=forms.URLInput(attrs={
        'placeholder': 'Enter URL here',
        'class': 'block w-full mt-1 p-2 border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50', 'rows': 4,
           
        }))


#forms for creating a user
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # field.widget.attrs['class'] = ' p-2.5 dark:bg-gray-sm-light'
            field.widget.attrs['placeholder'] = field.label
