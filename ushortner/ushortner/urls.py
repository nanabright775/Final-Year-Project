
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('urlshortner.urls')),
    path('', include('user.urls')),
    path('accounts/', include('allauth.urls')),
    path('chat/', include('chat.urls')),
    path('business_card/', include('business_card.urls')),
    path('detect/', include('detect.urls')),
    path('advertisements/', include('advertisements.urls')),
    path('landing/', include('landing_pages.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


