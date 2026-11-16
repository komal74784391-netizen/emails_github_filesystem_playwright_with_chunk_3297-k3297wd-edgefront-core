# FluxProxy 2.4.0 soak notes

Environment: 4 gateways behind the staging LB, 500 rps steady, 30 minutes.

- p99 added latency: 11.4 ms
- error rate: 0.002 %
- memory high-water mark: 412 MiB / pod

No regressions against 2.3.x.
