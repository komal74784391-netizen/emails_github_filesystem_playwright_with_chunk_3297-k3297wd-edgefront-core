"""Routing table behaviour."""
from fluxproxy.routing import RouteTable


def test_longest_prefix_wins():
    table = RouteTable()
    table.add("/api", lambda r: "shallow")
    table.add("/api/v2", lambda r: "deep")
    assert table.match("/api/v2/items").prefix == "/api/v2"


def test_unmatched_path():
    table = RouteTable()
    table.add("/api", lambda r: "shallow")
    assert table.match("/metrics") is None
