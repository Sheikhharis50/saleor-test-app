from django.http.request import HttpRequest
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import inspect


class AsyncView(View):
    async def dispatch(self, request: HttpRequest, *args, **kwargs):
        if inspect.iscoroutinefunction(getattr(self, request.method.lower(), None)):
            return await super().dispatch(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)


class AsyncViewNoCSRF(AsyncView):
    @csrf_exempt
    async def dispatch(self, request: HttpRequest, *args, **kwargs):
        return await super().dispatch(request, *args, **kwargs)
