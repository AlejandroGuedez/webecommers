from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from typing import Callable

class TenantMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable):
        host = request.headers.get("host", "")
        subdomain = host.split(".")[0]
        tenant = request.headers.get("X-Tenant", subdomain)
        request.state.tenant = tenant
        response = await call_next(request)
        return response
