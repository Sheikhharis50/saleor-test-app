from django.http import JsonResponse
from django.http.request import HttpRequest
import json

from app_core.views import AsyncViewNoCSRF
from app_auth.models import App


class WebhookView(AsyncViewNoCSRF):
    async def post(self, request: HttpRequest, app_name: str):
        payload = json.loads(request.body) if request.body else {}

        try:
            app = await App.objects.aget(name=app_name)
        except App.DoesNotExist:
            return JsonResponse(data={"error": "App not exists!"}, status=400)

        print(payload)

        return JsonResponse(data={"message": f"It is {app.name} App."})
