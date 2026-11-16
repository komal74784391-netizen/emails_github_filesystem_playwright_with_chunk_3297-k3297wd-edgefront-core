"""Prefix routing table with longest-match semantics."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict


@dataclass(frozen=True)
class Route:
    prefix: str
    upstream: Callable
    timeout_s: float = 2.5


class RouteTable:
    def __init__(self):
        self._routes: Dict[str, Route] = {}

    def add(self, prefix: str, upstream: Callable, timeout_s: float = 2.5):
        self._routes[prefix.rstrip("/")] = Route(prefix.rstrip("/"), upstream, timeout_s)

    def match(self, path: str):
        best = None
        for prefix, route in self._routes.items():
            if path.startswith(prefix) and (best is None or len(prefix) > len(best.prefix)):
                best = route
        return best

    def describe(self):
        return sorted(self._routes)
