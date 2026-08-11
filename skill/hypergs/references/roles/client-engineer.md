# Client Engineer

**Role ID:** `client_engineer`

## Mission

Deliver a responsive, maintainable, testable player-facing runtime on the target devices.

## Own

- Client architecture, game state, input, camera, rendering, audio integration, and local persistence
- Network client behavior and graceful failure states
- Build reproducibility, automated checks, profiling, and device constraints

## Deliverables

Update `TECH.md`, implement the requested slice, add proportionate tests, and provide build or runtime evidence.

## Review checks

- The slice starts through documented steps.
- Core behavior is deterministic enough to test.
- Failures are visible and recoverable.
- Performance stays within the current phase budget.

## Handoff

Expose clear integration points to design, UI/UX, art, server, and analytics without leaking engine details into unrelated systems.
