from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("CentralIdentityPlatformm/", include("CentralIdentityPlatformm.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
