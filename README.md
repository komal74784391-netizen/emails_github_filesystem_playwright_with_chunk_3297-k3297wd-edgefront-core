# FluxProxy Core

Reference implementation of the FluxProxy edge gateway.

`catalog_ref: fluxproxy` - this repository backs the capability-registry entry
`catalog/fluxproxy.md`.

## Availability

Public. Signed builds are cut from `main` and published to the public package
index; the current channel state is recorded in `distribution.json`.

## Layout

- `src/` gateway and routing code
- `tests/` unit tests
- `results/` load and soak notes
