from django.db import models
from django.contrib.auth.models import User

#models for bussiness card template
class BusinessCardTemplate(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='business_card_templates/')

    def __str__(self):
        return self.name

#models for bussiness card
class UserBusinessCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(BusinessCardTemplate, on_delete=models.CASCADE, blank=True, null=True)
    custom_template_image = models.ImageField(upload_to='custom_templates/', blank=True, null=True)
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
