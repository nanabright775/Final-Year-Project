# business_card/models.py

from django.db import models
from django.contrib.auth.models import User

class BusinessCardTemplate(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='business_card_templates/')

    def __str__(self):
        return self.name

class UserBusinessCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(BusinessCardTemplate, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Business Card"
