from django.contrib import admin
from .models import Campaign, Reel, Like, Comment

# Registering models .
admin.site.register(Campaign)
admin.site.register(Reel)
admin.site.register(Like)
admin.site.register(Comment)