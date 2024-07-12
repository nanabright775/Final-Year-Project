from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

THEME_CHOICES = [
    ('theme1', 'Theme 1'),
    ('theme2', 'Theme 2'),
    ('theme3', 'Theme 3'),
    ('theme4', 'Theme 4'),
    ('theme5', 'Theme 5'),
    ('theme6', 'Theme 6'),
    ('theme7', 'Theme 7'),
    ('theme8', 'Theme 8'),
]

LAYOUT_CHOICES = [
    ('layout1', 'Layout 1'),
    ('layout2', 'Layout 2'),
    ('layout3', 'Layout 3'),
    ('layout4', 'Layout 4'),
    ('layout5', 'Layout 5'),
]

FONT_CHOICES = [
    ('font1', 'Font 1'),
    ('font2', 'Font 2'),
    ('font3', 'Font 3'),
    ('font4', 'Font 4'),
    ('font5', 'Font 5'),
]

class LandingPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    welMessage = models.CharField(max_length=300, blank=True, null=True)
    contact = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    bussiness_name = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    theme = models.CharField(max_length=50, choices=THEME_CHOICES, blank=True, null=True)
    layout = models.CharField(max_length=50, choices=LAYOUT_CHOICES, blank=True, null=True)
    background_color = models.CharField(max_length=7, default='#ffffff')
    background_image = models.ImageField(upload_to='background_images/', blank=True, null=True)
    text_color = models.CharField(max_length=7, default='#000000')
    font_style = models.CharField(max_length=50, choices=FONT_CHOICES, blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    additional_image_1 = models.ImageField(upload_to='additional_images/', blank=True, null=True)
    additional_image_2 = models.ImageField(upload_to='additional_images/', blank=True, null=True)
    additional_image_3 = models.ImageField(upload_to='additional_images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    slug = models.SlugField(unique=True)

    

    def __str__(self):
        return self.title
