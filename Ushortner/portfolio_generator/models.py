from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.URLField(blank=True, null=True)
    # Additional fields for the generated portfolio
