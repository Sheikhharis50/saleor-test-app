from django.http import JsonResponse
from django.http.request import HttpRequest
from asgiref.sync import sync_to_async
import json

from app_core.views import AsyncViewNoCSRF
from .models import App


class RegisterView(AsyncViewNoCSRF):
    model = App

    async def post(self, request: HttpRequest):
        payload = json.loads(request.body)
        app_name = request.GET.get("app_name", "")

        app, _ = await self.model.objects.aget_or_create(name=app_name)
        app.token = payload.get("auth_token", "")
        await sync_to_async(app.save)(update_fields=["token"])

        return JsonResponse(data={"message": "registered."}, status=200)

    async def get(self, request: HttpRequest):
        app_name = request.GET.get("app_name")
        if app_name:
            try:
                app = await self.model.objects.aget(name=app_name)
                return JsonResponse(
                    {"data": {"name": app.name, "token": app.token}}, status=400
                )
            except self.model.DoesNotExist:
                pass
        return JsonResponse({"error": "app not registered"}, status=400)
