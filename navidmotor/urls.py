from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path("admin/", admin.site.urls),
]
urlpatterns += i18n_patterns(
    path("", include("core.urls")),
    path("salesnetwork/", include("salesnetwork.urls")),
    path("products/", include("products.urls")),
    path("solutions/", include("solutions.urls")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
