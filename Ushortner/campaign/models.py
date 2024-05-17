from django.db import models
from django.contrib.auth.models import User

class Campaign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='campaign_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description[:100]

