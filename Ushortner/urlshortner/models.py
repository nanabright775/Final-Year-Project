from django.db import models
from user_agents import parse as ua_parse
from user.models import User 

# Models for a short url
class ShortURL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    clicks = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    qr_code_data = models.TextField(null=True, blank=True)  

    
    def __str__(self):
        return self.short_code
        
    class Meta:
        ordering = ['-date_created'] 

#models for clicks to provide analytics
class Click(models.Model):
    short_url = models.ForeignKey(ShortURL, on_delete=models.CASCADE)
    user_agent_string = models.CharField(max_length=255)
    referer = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    browser = models.CharField(max_length=100, null=True, blank=True)
    device = models.CharField(max_length=100, null=True, blank=True)
    click_count = models.IntegerField(default=0)


    def save(self, *args, **kwargs):
        parsed_user_agent = ua_parse(self.user_agent_string)
        self.browser = parsed_user_agent.browser.family
        self.device = parsed_user_agent.device.family
        super().save(*args, **kwargs)


    def increase_clicks(self):
        self.click_count += 1
        self.save(update_fields=['click_count'])
        
    def __str__(self):
        return f"{self.timestamp} {self.ip_address} {self.browser} {self.device}"