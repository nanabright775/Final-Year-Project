# business_card/admin.py

from django.contrib import admin
from .models import BusinessCardTemplate, UserBusinessCard

admin.site.register(BusinessCardTemplate)
admin.site.register(UserBusinessCard)
