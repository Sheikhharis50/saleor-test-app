from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("app_auth.urls")),
    path("api/v1/webhook/", include("app_webhook.urls")),
]
