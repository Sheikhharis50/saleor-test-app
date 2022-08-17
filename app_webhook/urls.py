from django.urls import path

from .views import (
    WebhookView,
)

urlpatterns = [
    path("<str:app_name>", WebhookView.as_view(), name="webhook"),
]
