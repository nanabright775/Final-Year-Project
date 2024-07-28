from django.db import models
from django.contrib.auth.models import User

#models for messages
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)  

    
    def __str__(self):
        return f"{self.sender} to {self.receiver} - {self.content[:20]}"
