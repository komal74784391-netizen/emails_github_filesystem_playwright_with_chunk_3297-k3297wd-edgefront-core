"""FluxProxy gateway: request entry point."""
from __future__ import annotations

import asyncio
import logging

from .routing import RouteTable

LOG = logging.getLogger("fluxproxy.gateway")


class Gateway:
    """Front-door object that owns the listener and the route table."""

    def __init__(self, routes: RouteTable, quota_per_minute: int = 600):
        self.routes = routes
        self.quota_per_minute = quota_per_minute
        self._in_flight = 0

    async def handle(self, request):
        route = self.routes.match(request.path)
        if route is None:
            raise LookupError(f"no route for {request.path}")
        self._in_flight += 1
        try:
            return await asyncio.wait_for(route.upstream(request), timeout=route.timeout_s)
        finally:
            self._in_flight -= 1

    def snapshot(self):
        return {"in_flight": self._in_flight, "routes": self.routes.describe()}
