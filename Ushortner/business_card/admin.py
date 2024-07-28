
from django.contrib import admin
from .models import BusinessCardTemplate, UserBusinessCard

#registering models
admin.site.register(BusinessCardTemplate)
admin.site.register(UserBusinessCard)
