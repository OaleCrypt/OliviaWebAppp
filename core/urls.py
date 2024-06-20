from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('olivia_le.urls')),
    path('password-manager/', include('password_manager.urls')),
    path('soc/', include('soc.urls')),
    path('integrations/', include('integrations.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
