from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("", include("users.urls")),
    path("", include("app.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = "pages.views.error_404_view"
handler500 = "pages.views.error_500_view"
