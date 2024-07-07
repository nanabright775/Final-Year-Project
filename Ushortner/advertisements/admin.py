from django.contrib import admin
from .models import Campaign, Reel, Like, Comment
# Register your models here.
admin.site.register(Campaign)
admin.site.register(Reel)
admin.site.register(Like)
admin.site.register(Comment)