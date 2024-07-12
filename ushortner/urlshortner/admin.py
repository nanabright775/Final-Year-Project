from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.ShortURL)
admin.site.register(models.Click)