from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls")),
    path("salesnetwork/", include("salesnetwork.urls")),
    path("products/", include("products.urls")),
    path("solutions/", include("solutions.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
